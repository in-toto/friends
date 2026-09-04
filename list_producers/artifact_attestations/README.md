---
type: Database
besides: No
format: [sigstore bundle]
visibility: [Public, Private]
---

# Github Artifact Attestations

Attestations are generated for workflows using the [`attest`](https://github.com/actions/attest), [`attest-build-provenance`](https://github.com/actions/attest-build-provenance), and [`attest-sbom`](https://github.com/actions/attest-sbom) created by GitHub and are stored for each repository in `https://github.com/{ORG}/{REPOSITORY}/attestations`. 

**References:** 

- <https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations>
- <https://docs.github.com/en/actions/concepts/security/artifact-attestations>
- <https://github.blog/news-insights/product-news/introducing-artifact-attestations-now-in-public-beta/>
- <https://docs.github.com/en/rest/users/attestations?apiVersion=2022-11-28>
