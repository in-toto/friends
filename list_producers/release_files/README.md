---
type: Repository
besides: Yes
format: [Any]
visibility: [Public, Private]
---

# Github Release Files

Different tools can generate in-toto attestations as a file in a release. For example, the [`slsa github generator`](https://github.com/slsa-framework/slsa-github-generator) generates attestations in a release. Certain file naming formats are used, such as files that end with `intoto.jsonl`.  Additionally, tools are using these attestations to check if releases are signed, such as in [`OpenSSF Scorecard`](https://github.com/ossf/scorecard/blob/main/docs/checks.md#signed-releases).

**References:** 

- <https://slsa.dev/spec/v1.2/distributing-provenance>
- <https://github.com/ossf/scorecard/blob/main/docs/checks.md#signed-releases>