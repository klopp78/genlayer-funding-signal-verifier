# Funding Signal Verifier

Funding Signal Verifier is a GenLayer Intelligent Contract for checking whether public funding, grant, acquisition, accelerator, or partnership claims are backed by concrete evidence.

It is built for crypto and AI research workflows where users often see posts such as "Project X raised $12M" or "Project Y is backed by Fund Z" and need a compact, consensus-backed signal before treating the claim as reliable.

## What It Does

The contract accepts:

- a funding or partnership claim
- two to five public source URLs

It stores a structured result:

- `signal`: `confirmed`, `partial`, `unverified`, or `contradicted`
- `confidence`: 0-100
- `amount_found`: whether a funding/deal amount was directly found
- `investor_found`: whether investor, grantor, partner, or counterparty names were directly found
- `official_source_count`: number of primary or official sources
- `risk_level`: `low`, `medium`, or `high`
- `summary`

## Why This Fits GenLayer

This is not a plain scraper. The contract uses GenLayer's nondeterministic web rendering and LLM interpretation, then asks validators to independently rerun the funding-signal analysis.

Consensus compares stable fields:

- exact `signal`
- exact `risk_level`
- exact amount/investor booleans
- confidence within 18 points
- official source count within one source

That gives builders a reusable primitive for judging high-velocity market claims without trusting a single generated answer.

## Contract

```text
contracts/funding_signal_verifier.py
```

Main write method:

```python
verify_signal(claim: str, source_urls: DynArray[str])
```

Main view method:

```python
get_latest_signal() -> str
```

## Example Input

```text
Claim:
Axis Robotics raised a 12 million dollar seed round led by reputable investors.

Sources:
https://project.example/blog/seed-round
https://x.com/project/status/...
https://fund.example/news/project-investment
```

Example output:

```json
{"amount_found":true,"confidence":84,"investor_found":true,"official_source_count":2,"risk_level":"low","signal":"confirmed","summary":"Two primary sources state the round amount and name investors, while the social post repeats the same announcement."}
```

## Reviewer Notes

Funding claims are especially useful for GenLayer because the right answer often depends on live public web context, source credibility, and whether details are primary or repeated secondhand.

The validator does more than check JSON shape. It independently reviews the same URLs and compares the durable decision fields that matter for downstream applications.
