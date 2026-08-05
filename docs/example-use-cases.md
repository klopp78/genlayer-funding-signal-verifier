# Example Use Cases

## Research Desk

A crypto research team sees a claim that a project raised a new seed round. The team submits the claim with the project's blog post, an investor announcement, and the original X post. The contract returns a confirmed signal when primary evidence supports the amount and investor names.

## Grant Review

A grant team wants to verify whether an applicant has received ecosystem funding from another foundation. The reviewer submits the applicant claim and public grant pages. The contract returns partial or unverified if the amount or grantor is not directly supported.

## Launchpad Due Diligence

A launchpad screens projects that claim strategic partnerships. The launchpad submits the announcement and partner-side sources. The contract flags higher risk when the claim is repeated by the applicant but missing from the partner's official channels.

## Market Intelligence Dashboard

A dashboard monitors funding and partnership announcements across crypto and AI. Instead of showing raw rumors, it stores GenLayer-backed labels such as confirmed, partial, unverified, or contradicted with concise explanations.

## Contradicted Claim

A project claims it was acquired, but a primary source denies the acquisition or describes it as a non-binding collaboration. The verifier can return `contradicted` when a strong source directly disputes the submitted claim.
