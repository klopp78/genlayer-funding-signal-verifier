# Contributing

Contributions should improve the contract, test coverage, examples, or documentation for funding-signal verification.

## Useful Contributions

- Add realistic sample claims and source sets.
- Improve source classification logic.
- Add claim-history storage and view methods.
- Build a small CLI or web demo.
- Write integration notes for researchers, grant teams, or dashboards.
- Improve README clarity and architecture diagrams.

## Development Notes

Keep contract outputs stable. Downstream users should be able to rely on these fields:

- `signal`
- `confidence`
- `amount_found`
- `investor_found`
- `official_source_count`
- `risk_level`
- `summary`

When changing validator agreement logic, document why the fields should be strict or tolerant. The current implementation requires exact agreement on `signal`, `risk_level`, and key booleans, while allowing limited tolerance for `confidence` and official source count.

## Issue Ideas

Good first issues:

- Add `get_latest_claim()` view method.
- Add sample input for a contradicted funding claim.
- Add examples for grant and partnership announcements.
- Document expected behavior for inaccessible sources.

Larger issues:

- Add persistent claim history by ID.
- Add source-type classification.
- Build a simple demo client.
- Design token-based request and staking flows.
