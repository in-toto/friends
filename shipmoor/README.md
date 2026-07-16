# Shipmoor

[Shipmoor](https://shipmoor.dev) is a local, vendor-neutral verification layer for AI-agent-written code. Its [Claim Check](https://shipmoor.dev/claim-check) feature freezes a change's stated intent into an acceptance set of atomic, checkable obligations, then binds each one to real evidence: the build, the test suite, deterministic scans, and an advisory code review.

Every piece of that evidence is wrapped in an [in-toto attestation](https://github.com/in-toto/attestation). The resulting verdict (`READY`, `READY WITH GAPS`, `BLOCKED`, or `INCONCLUSIVE`) ships as a SLSA-shaped Verification Summary Attestation (VSA) with a self-digest. Rather than trusting a rerun's word for it, Shipmoor checks whether two runs match byte-for-byte.

The whole loop runs locally: no model is hosted or called by Shipmoor, and no source code is uploaded. See [how Claim Check works](https://docs.shipmoor.dev/docs/claim-check/overview) for the full design, including the [bring-your-own-judge model](https://docs.shipmoor.dev/docs/claim-check/byo-judge) used for the obligations a deterministic check can't yet reach.
