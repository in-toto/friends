---
type: Package Registry
besides: Yes
format: [sigstore bundle]
visibility: [Public]
---

# npm

[npm](https://npmjs.com/)  stores attestations that can be accessed through the API as `https://registry.npmjs.org/-/npm/v1/attestations/{PACKAGE}@{VERSION}`. Note, some prior versions used Sigstore Rekor to store attestations.

**References:** 

- <https://docs.npmjs.com/generating-provenance-statements>
- <https://github.blog/security/supply-chain-security/introducing-npm-package-provenance/>