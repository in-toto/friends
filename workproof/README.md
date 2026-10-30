# workproof

[workproof](https://github.com/Bubblegunn/workproof) turns one author's history in a git repository,
including a private one, into a report of figures computed from git (surviving lines, commits, tenure
and others), without showing any code. The report carries a hash: sha256 over the RFC 8785 canonical
JSON of its parameters and figures, which anyone holding the report can recompute offline with
`workproof check`.

## How it uses in-toto

`workproof attest report.json` writes an [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md):

- **subject**: one entry, `workproof-report`, whose `sha256` digest is the report's hash. The figures
  sit behind that digest rather than in the predicate.
- **predicateType**: `https://github.com/Bubblegunn/workproof/blob/main/docs/attestation-v1.md`, which
  documents every field.
- **predicate**: the tool version, the parameters, and per repository the commit the figures were
  computed at, a repository fingerprint, the author names covered, the git version and blame flags,
  and what was excluded (bot commits, generated files). It carries no figures, paths, remote URL or
  email address, and the project's tests check that.

In the project's GitHub Action, `attest: "true"` signs the same Statement keylessly with Sigstore
(`cosign attest-blob`), and a reader verifies it with `cosign verify-blob-attestation`. Without the
Action, `--local <ssh-key>` signs it with an SSH key.

What is unusual about it: the attestation is about authorship of work in a repository the verifier may
not be able to see, rather than about a build artifact.
