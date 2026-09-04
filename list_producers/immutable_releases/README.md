---
type: Repository
besides: Yes
format: [sigstore bundle]
visibility: [Public, Private]
---

# Github Immutable Releases

GitHub provides a feature to prevent changes in releases (immutable releases) that can be configured for organizations and repositories. The attestations are stored in the releases that were configured to be immutable. Note, although Immutable Releases downloaded link references the location in artifact attestations, they are not found in the list provided within the GitHub webpage.

**References:** 

- <https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/>
- <https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/preventing-changes-to-your-releases>
- <https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verifying-the-integrity-of-a-release>
- <https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases>