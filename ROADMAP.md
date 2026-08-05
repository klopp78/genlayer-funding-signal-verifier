# Roadmap

Funding Signal Verifier is currently an early GenLayer Intelligent Contract prototype. The roadmap below keeps the scope narrow enough to build, while showing how the project can become useful infrastructure for market-signal verification.

## Current Version

- Accept a funding, grant, acquisition, accelerator, or partnership claim.
- Accept two to five public source URLs.
- Render source pages through GenLayer nondeterministic web access.
- Ask validators to independently evaluate the claim.
- Store a compact JSON signal with confidence, source count, risk level, and summary.

## Near-Term Milestones

### M1: Claim History

- Add a `check_id` for every submitted claim.
- Store historical signals instead of only `latest_signal`.
- Add `get_signal(check_id)` and `get_claim_count()` view methods.
- Include source URL count and timestamp-like metadata when available.

### M2: Better Source Classification

- Classify sources as official, primary media, secondary media, social, or weak.
- Penalize unsupported reposts.
- Improve confidence scoring when sources disagree.
- Document examples for confirmed, partial, unverified, and contradicted claims.

### M3: Developer Demo

- Add a minimal CLI or web form for submitting a claim and URLs.
- Show the returned JSON in a readable report format.
- Include sample workflows for researchers and grant reviewers.
- Add screenshots or a short demo recording.

### M4: API and Dataset Layer

- Add a read API for historical verified signals.
- Support batch verification for watchlists.
- Export normalized signal records for dashboards.
- Track repeated checks as public evidence evolves.

## Long-Term Direction

The long-term goal is a reusable verification layer for crypto and AI market claims. Funding checks are the first vertical because they have clear fields: amount, investor or partner, primary source count, confidence, and risk.

After funding signals, the same pattern can expand to:

- partnership verification
- grant award verification
- team credential checks
- ecosystem participation claims
- due-diligence records for launchpads and accelerators

## Open Questions

- What source policies should count as official or primary?
- How should the contract handle inaccessible or paywalled pages?
- Which fields should be strict consensus fields versus flexible explanation fields?
- Should disputes be handled by repeated checks, staked reviewers, or governance votes?
