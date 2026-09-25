# agent-change-control

[agent-change-control](https://github.com/noru-tech/agent-change-control) (`acc`) enforces the
four-eyes principle for changes written with coding agents. When an agent opens a pull request and
the engineer who directed it approves, the platform sees two accounts and one human judgment. `acc`
records the agent, its human operator, the reviewers and the merger, and evaluates offline and
deterministically whether a human independent of the effective author approved the current head
before merge. Unknown stays unknown, and incomplete collection can never produce a clean result.

## How it uses in-toto

`acc` is both a producer and a consumer of in-toto attestations.

**Producer.** `acc … --format in-toto` emits an unsigned
[Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) whose
subjects are the change's head commit and, once merged, its merge commit (`gitCommit` digests), and
whose predicate (`https://noru.tech/spec/ai-change-provenance/v0.2`) is the full evaluated manifest:
the normalized facts with evidence references, the resolved policy, the findings and per-rule
assessments. `--format in-toto-jsonl` writes one Statement per change. Signing is left to the
signer the organization already trusts: the repository's own workflow attests the verdict of every
merged pull request through GitHub artifact attestations, and `cosign attest-blob --statement`
signs the commit-subject form. `acc validate` on a Statement checks that the subjects fit the
predicate and re-evaluates the predicate, requiring byte-identical findings, so a verifier can
confirm the verdict follows from the embedded facts rather than trust it.

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

The predicate is documented in the in-toto predicate template in
[`docs/in-toto.md`](https://github.com/noru-tech/agent-change-control/blob/main/docs/in-toto.md),
and the convention it implements is the
[AI Change Provenance](https://github.com/noru-tech/agent-change-control/blob/main/spec/ai-change-provenance.md)
specification.

## References

* https://github.com/noru-tech/agent-change-control
* https://github.com/noru-tech/agent-change-control/blob/main/docs/signing.md
* https://github.com/noru-tech/agent-change-control/attestations
