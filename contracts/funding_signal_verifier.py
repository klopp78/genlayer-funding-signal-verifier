# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import json
import typing


class FundingSignal(typing.NamedTuple):
    signal: str
    confidence: u8
    amount_found: bool
    investor_found: bool
    official_source_count: u8
    risk_level: str
    summary: str


class FundingSignalVerifier(gl.Contract):
    """Verifies whether a funding or partnership announcement is evidence-backed."""

    latest_claim: str
    latest_signal: str

    def __init__(self):
        self.latest_claim = ""
        self.latest_signal = ""

    @gl.public.view
    def get_latest_signal(self) -> str:
        return self.latest_signal

    @gl.public.write
    def verify_signal(self, claim: str, source_urls: DynArray[str]):
        if len(claim) < 16:
            raise Exception("claim is too short")
        if len(source_urls) < 2:
            raise Exception("at least two sources are required")
        if len(source_urls) > 5:
            raise Exception("use five sources or fewer")

        def leader_fn():
            return _verify_funding_signal(claim, source_urls)

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return):
                return False

            try:
                proposed = _parse_signal(leader_result.calldata)
                independent = _parse_signal(_verify_funding_signal(claim, source_urls))
            except Exception:
                return False

            if proposed.signal != independent.signal:
                return False
            if proposed.risk_level != independent.risk_level:
                return False
            if proposed.amount_found != independent.amount_found:
                return False
            if proposed.investor_found != independent.investor_found:
                return False

            confidence_delta = abs(int(proposed.confidence) - int(independent.confidence))
            source_delta = abs(
                int(proposed.official_source_count) - int(independent.official_source_count)
            )
            return confidence_delta <= 18 and source_delta <= 1

        agreed_json = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)
        self.latest_claim = claim
        self.latest_signal = agreed_json


def _verify_funding_signal(claim: str, source_urls: DynArray[str]) -> str:
    pages = []
    for url in source_urls:
        rendered = gl.nondet.web.render(url, mode="text")
        pages.append(
            {
                "url": url,
                "text": rendered[:6500],
            }
        )

    prompt = f"""
You are verifying a crypto or AI project funding, grant, acquisition, accelerator,
or strategic partnership claim. Evaluate whether the supplied public sources contain
specific evidence, not general project marketing.

Claim:
{claim}

Sources:
{json.dumps(pages)}

Return only minified JSON with exactly these keys:
- signal: one of "confirmed", "partial", "unverified", "contradicted"
- confidence: integer from 0 to 100
- amount_found: boolean, true only if a funding amount, grant size, or deal size is directly found
- investor_found: boolean, true only if investor, partner, grantor, or counterparty names are directly found
- official_source_count: number of supplied sources that appear official or primary
- risk_level: one of "low", "medium", "high"
- summary: concise explanation under 460 characters

Rules:
- "confirmed" requires direct evidence from an official source or a credible primary report.
- "partial" means some details are supported but important fields are missing.
- "unverified" means sources are weak, indirect, inaccessible, or only repeat the claim.
- "contradicted" means at least one strong source disputes the claim.
- Treat missing amount or missing investor/partner names as risk, not proof.
- Do not infer funding amounts from valuation, followers, or vague "backed by" language.
"""

    raw = gl.nondet.exec_prompt(prompt)
    data = json.loads(raw)
    normalized = {
        "signal": str(data["signal"]).lower(),
        "confidence": max(0, min(100, int(data["confidence"]))),
        "amount_found": bool(data["amount_found"]),
        "investor_found": bool(data["investor_found"]),
        "official_source_count": int(data["official_source_count"]),
        "risk_level": str(data["risk_level"]).lower(),
        "summary": str(data["summary"])[:460],
    }
    return json.dumps(normalized, sort_keys=True, separators=(",", ":"))


def _parse_signal(raw_json: str) -> FundingSignal:
    data = json.loads(raw_json)
    signal = str(data["signal"]).lower()
    risk_level = str(data["risk_level"]).lower()
    confidence = int(data["confidence"])
    official_source_count = int(data["official_source_count"])
    summary = str(data["summary"])

    if signal not in ("confirmed", "partial", "unverified", "contradicted"):
        raise Exception("invalid signal")
    if risk_level not in ("low", "medium", "high"):
        raise Exception("invalid risk level")
    if confidence < 0 or confidence > 100:
        raise Exception("invalid confidence")
    if official_source_count < 0 or official_source_count > 5:
        raise Exception("invalid official source count")
    if len(summary) == 0 or len(summary) > 460:
        raise Exception("invalid summary")

    return FundingSignal(
        signal=signal,
        confidence=u8(confidence),
        amount_found=bool(data["amount_found"]),
        investor_found=bool(data["investor_found"]),
        official_source_count=u8(official_source_count),
        risk_level=risk_level,
        summary=summary,
    )
