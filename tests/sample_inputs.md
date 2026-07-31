# Sample Inputs

## Confirmed Funding Signal

```text
Claim:
Example Project raised a 12 million dollar seed round with named investors.

Sources:
https://example-project.invalid/blog/seed-round
https://example-fund.invalid/news/example-project
https://x.com/example/status/123
```

Expected shape:

```json
{"signal":"confirmed","confidence":80,"amount_found":true,"investor_found":true,"official_source_count":2,"risk_level":"low","summary":"..."}
```

## Partial Signal

```text
Claim:
Example Project is backed by major funds and completed a new financing round.

Sources:
https://example-project.invalid/about
https://x.com/example/status/456
```

Expected shape:

```json
{"signal":"partial","confidence":55,"amount_found":false,"investor_found":true,"official_source_count":1,"risk_level":"medium","summary":"..."}
```

## Unverified Signal

```text
Claim:
Example Project raised an undisclosed eight-figure round.

Sources:
https://random-blog.invalid/example-project-rumor
https://x.com/unrelated/status/789
```

Expected shape:

```json
{"signal":"unverified","confidence":35,"amount_found":false,"investor_found":false,"official_source_count":0,"risk_level":"high","summary":"..."}
```
