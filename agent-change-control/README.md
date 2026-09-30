# agent-change-control

[agent-change-control](https://github.com/noru-tech/agent-change-control) (`acc`) enforces the
four-eyes principle for changes written with coding agents. When an agent opens a pull request and
the engineer who directed it approves, the platform sees two accounts and one human judgment. `acc`
records the agent, its human operator, the reviewers and the merger, and evaluates offline and
deterministically whether a human independent of the effective author approved the current head
before merge. Unknown stays unknown, and incomplete collection can never produce a clean result.
The current release is [v0.5.2](https://github.com/noru-tech/agent-change-control/releases/tag/v0.5.2),
implementing AI Change Provenance 0.3.

## How it uses in-toto

`acc` is both a producer and a consumer of in-toto attestations.

**Producer.** `acc … --format in-toto` emits an unsigned
[Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) whose
subjects are the change's head commit and, once merged, its merge commit (`gitCommit` digests), and
whose predicate (`https://noru.tech/spec/ai-change-provenance/v0.3`) is the full evaluated manifest:
the normalized facts with evidence references, the resolved policy, the findings and per-rule
assessments. `--format in-toto-jsonl` writes one Statement per change. Signing is left to the
signer the organization already trusts: the repository's own workflow attests the verdict of every
merged pull request through GitHub artifact attestations, and `cosign attest-blob --statement`
signs the commit-subject form. Every digest, including the finding identifiers and the `sha256`
subject form, is SHA-256 over the [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785)
serialization, so any JCS implementation reproduces it. `acc validate` on a Statement checks that
the subjects fit the predicate and re-evaluates the predicate, requiring byte-identical findings,
so a verifier can confirm the verdict follows from the embedded facts rather than trust it.
Statements made by earlier releases (`v0.2`) still validate.

**Consumer.** Two predicates of its own carry claims that `acc` reads back as evidence, both bound
to a change by its head commit and handed over pre-verified with a recorded verifier:

- `https://noru.tech/spec/ai-change-provenance/provenance/v0.1`, signed by an agent's integration
  or its operator, stating which agent wrote the change and which human directed it.
- `https://noru.tech/spec/ai-change-provenance/review/v0.1`, signed by a reviewer's tooling,
  stating who reviewed what and decided what. It names the reviewer in the predicate so that a
  consumer working from pre-verified input can use it, and for an agent reviewer it records the
  operator, the instructions owner and the model.

Evidence carries its strength (`derived < declared < observed < signed`), a policy can set the
minimum it accepts, and, opt-in, an agent's signed approval can satisfy independence when it is
independent of the author's operator, vendor and verified signing identity.

**Conformance.** Evaluator conformance is defined by a published corpus rather than by agreement
with `acc`: accept, reject and incomplete vectors run through an external-verifier contract
(`<cmd> <vector-file>`, the verdict in the exit status, one JSON result line), with a
standard-library harness and a GitHub Action. Suite revision 2 has its digest list signed at
v0.5.2 with a GitHub artifact attestation. See
[`conformance/`](https://github.com/noru-tech/agent-change-control/tree/v0.5.2/conformance).

**Predicate registration.** All three predicates are proposed as community contributions to
in-toto/attestation: the evaluation predicate
([#601](https://github.com/in-toto/attestation/pull/601)), authorship
([#602](https://github.com/in-toto/attestation/pull/602)) and review
([#603](https://github.com/in-toto/attestation/pull/603)).

The predicate is documented in the in-toto predicate template in
[`docs/in-toto.md`](https://github.com/noru-tech/agent-change-control/blob/main/docs/in-toto.md),
and the convention it implements is the
[AI Change Provenance](https://github.com/noru-tech/agent-change-control/blob/main/spec/ai-change-provenance.md)
specification.

## References

* https://github.com/noru-tech/agent-change-control
* https://github.com/noru-tech/agent-change-control/blob/main/docs/signing.md
* https://github.com/noru-tech/agent-change-control/attestations
* https://github.com/noru-tech/agent-change-control/tree/v0.5.2/conformance
* https://doi.org/10.5281/zenodo.23042500 (Zenodo archive of every release)
