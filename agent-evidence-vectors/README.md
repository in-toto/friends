# Agent Evidence Vectors

[agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors) is a conformance
vector suite and reference verifier for evidence about what an automated agent did at run time.
The ten corpus manifests at release v0.12.0 sum to 736 vectors, judged by one Go verifier,
`aee-verify`, selected by the suite each corpus manifest declares.

## How it uses in-toto

Every vector is an in-toto Statement, and two of the ten corpora exercise proposed predicates
directly:

- `vectors/` implements the **adversarial-execution-evidence** predicate proposed in
  [in-toto/attestation#570](https://github.com/in-toto/attestation/pull/570), at predicate
  version 0.7. The corpus splits 61 accept, 209 reject and 2 indeterminate.
- `vectors-ai-agent-action/` implements the **ai-agent-action** predicate proposed in
  [in-toto/attestation#588](https://github.com/in-toto/attestation/pull/588), at predicate
  version 0.1, and carries the canonicalization strengthening this project offers into that
  pull request. The corpus splits 37 accept and 16 reject.
- `vectors-scitt-cose/` tests how an adversarial-execution-evidence Statement is carried as an
  IETF SCITT Transparent Statement, signed as a COSE_Sign1 and proved by an RFC 9942 Receipt.
  Four of its 27 members are indeterminate on purpose: each records a question RFC 9943 and
  RFC 9942 leave open, and the readings a conforming verifier could take.

The predicate text is vendored under `spec/predicates/` with the upstream commit it was taken
from recorded in `spec/VENDOR-PIN.json`. `CITATION.cff` states that the suite carries no standing
as a standard of its own: the normative artifact is the predicate's own text, settled upstream.

## Why the suite exists

The predicate's model is execute-and-attest rather than match-and-assert. A consumer recomputes
the outcome from the bytes the Statement carries, so a producer that asserts a verdict about
itself can be refused. That property is only worth anything if two independent verifiers of the
same predicate either agree byte for byte or are shown exactly where they diverge, and a corpus
is what forces the question.

`RUNS.md` records runs by implementations this project did not write. The row there today is
`Rul1an/aee-checker`, an independent Rust verifier with its own I-JSON parser, RFC 8785
serializer, RFC 6962 Merkle root and Ed25519 tier, which replayed the corpus at suite revision 27
and returned 61/61 accepts, 209/209 rejects and 2/2 indeterminate with zero mismatches,
posted at Rul1an/aee-checker#21. That row
carries the directed label its own author gave it, and what the run does not cover.

## Details

- Licence: Apache-2.0
- Archived at Zenodo, DOI [10.5281/zenodo.22758687](https://doi.org/10.5281/zenodo.22758687)
- Reference verifier: `cmd/aee-verify`, Go
