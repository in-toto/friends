# Trustabl

[Trustabl](https://trustabl.ai) is a static analyzer for AI-agent codebases. It inventories the agents, tools, subagents, skills and MCP servers in a repository and evaluates each one against a versioned rule pack covering nine agent SDKs, looking for the failure modes ordinary review misses: a tool that shells out and can be prompt-injected, an agent session with no turn limit, a tool that fetches a caller-controlled URL.

A scan result can be signed into an [in-toto attestation](https://github.com/in-toto/attestation) with `trustabl attest`. The predicate is built deterministically from the scan report and carries the predicate type `https://trustabl.dev/attestation/scan/v1`, with the report itself as the attestation subject. Signing is keyless by default, using the CI runner's ambient OIDC identity and recording the signature in Rekor; `--key` with `--no-tlog` covers offline and air-gapped signing that must not reach a public log. `trustabl verify` checks an attestation back against its report.

What this buys a verifier is evidence rather than assertion. The attestation records which ruleset an agent repository was checked against and what the scan concluded, so a consumer can establish that the check actually happened, against a known set of rules, before the agent shipped. The subject is the scanned repository's result, not the Trustabl binary, and the signer is whoever ran the command.

Scanning runs entirely on the user's machine. There is no hosted scanner, no account, and no source code upload. See the [attestation format](https://github.com/trustabl/agent-reliability-analyzer/blob/main/docs/attestation.md) for the predicate schema and verification steps.
