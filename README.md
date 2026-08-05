# Funding Signal Verifier

Funding Signal Verifier is a GenLayer Intelligent Contract for checking whether public funding, grant, acquisition, accelerator, or partnership claims are backed by concrete evidence.

It is built for crypto and AI research workflows where users often see posts such as "Project X raised $12M" or "Project Y is backed by Fund Z" and need a compact, consensus-backed signal before treating the claim as reliable.

## Problem

Funding and partnership announcements move quickly across X posts, blogs, launchpad pages, press releases, grant dashboards, and investor sites. A single repeated claim can look credible before anyone checks whether the amount, investor names, or primary source actually exist.

Research teams, traders, grant reviewers, launchpads, and protocols need a repeatable way to separate:

- confirmed announcements with primary evidence
- partial claims where some fields are supported
- unverified reposts or low-quality sources
- contradicted claims where strong sources disagree

## Solution

This project turns a public market claim and a small set of source URLs into a structured funding signal. Instead of trusting one scraper or one LLM answer, the contract asks GenLayer validators to independently review the same sources and agree on durable decision fields.

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

## Target Users

- crypto and AI researchers validating announcements before writing reports
- grant teams checking whether applicants have public funding or partner evidence
- launchpads and accelerators screening project traction claims
- trading and intelligence dashboards that need explainable signal labels
- protocols that want a reusable verification component for due diligence

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

## Token Model

The long-term token model can align demand for claim checks with validator and reviewer incentives:

- request fees: users or protocols spend credits or tokens to request funding signal checks
- staking: verification agents or reviewers stake tokens to participate in dispute resolution and source quality review
- priority access: token holders can prioritize urgent market-signal checks or batch verification jobs
- dataset access: tokens can unlock historical verified-signal datasets and API tiers
- governance: token holders can vote on accepted source policies, risk-weighting rules, dispute windows, and supported claim types

The token is not required for the first contract prototype. The immediate goal is to prove that funding and partnership claims can be evaluated consistently through GenLayer consensus before introducing economic incentives.

## Roadmap

### Phase 1: Contract Prototype

- define stable signal schema
- validate 2-5 source URLs per claim
- compare independent validator outputs
- store latest verified result on-chain

### Phase 2: Evidence Registry

- store historical claim checks by ID
- add query methods for past signals
- include source fingerprints and timestamps
- support repeat checks when public evidence changes

### Phase 3: Developer API and Dashboard

- expose a simple API for dashboards and due-diligence tools
- add example integrations for research workflows
- provide batch checks for funding, grant, and partnership announcements

### Phase 4: Incentives and Governance

- introduce request fees and staking-based review flows
- add source-policy governance
- support disputes for ambiguous or contradictory claims
- expand beyond funding signals into team credential and partnership verification

## Repository Status

This repository is an early-stage GenLayer prototype. The current implementation focuses on one contract and representative sample inputs. The next useful contributions are:

- realistic test cases using public funding or grant announcements
- contract methods for storing signal history by claim ID
- a minimal CLI or web demo for submitting claims
- source-quality heuristics for official, primary, and secondary sources

## Reviewer Notes

Funding claims are especially useful for GenLayer because the right answer often depends on live public web context, source credibility, and whether details are primary or repeated secondhand.

The validator does more than check JSON shape. It independently reviews the same URLs and compares the durable decision fields that matter for downstream applications.
