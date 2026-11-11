# proofbundle

[proofbundle](https://github.com/b7n0de/proofbundle) is an MIT-licensed Python tool that turns test runs and AI evaluation results into signed receipts. Its native receipt format can be verified offline from a single JSON file, without a verification server. It ships plugins for pytest and [Inspect AI](https://inspect.aisi.org.uk/).

proofbundle uses in-toto to export evaluation claims for use in software supply chain workflows. The `proofbundle intoto` command exports an [in-toto Statement](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) in a DSSE envelope signed with Ed25519. It defaults to eval-result v0.1. To export v0.2, select `--predicate-version v0.2` and supply the evaluation party with `--evaluator <URI>`. The `proofbundle intoto --verify` command verifies either version against the public key supplied with `--pub`.

The eval-result predicate records the metric, comparator, threshold and reported pass or fail verdict. Salted commitments can keep the model and dataset identifiers private. Version 0.2 uses the vendor predicate type `https://b7n0de.com/attestation/eval-result/v0.2`. The predicate is proposed in [in-toto/attestation#575](https://github.com/in-toto/attestation/pull/575), which has not been merged.

For a valid evaluation receipt with a passing verdict, `proofbundle svr` emits a separate signed Summary Verification Result using `svr/v0.1`. The Python function `to_test_result_statement` can also map an evaluation claim to the community `test-result/v0.1` predicate.

Verification checks the signature over the signed payload. It does not establish that the reported result is true or that the evaluation was sound. Trust in the signing key is a separate decision. See [what proofbundle does not claim](https://github.com/b7n0de/proofbundle/blob/v6.5.0/docs/NON_CLAIMS.md).

The project website is [proofbundle.dev](https://proofbundle.dev/).
