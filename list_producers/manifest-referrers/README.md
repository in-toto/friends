---
type: Images
besides: Either
format: [Any]
visibility: [Public, Private]
---

# Manifest Referrers API

Containers following the [Open Container Initiative (OCI)](https://opencontainers.org/) can specify, within a [Manifest Reffers API](https://github.com/oras-project/artifacts-spec/blob/main/manifest-referrers-api.md), the location for consumers. Attestations can be collected with tools such as [`cosign`](https://github.com/sigstore/cosign) and [`crane`](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md). The attestations may be stored in any format, although formats such as ["Cosign Bundle"](https://github.com/sigstore/cosign/blob/main/specs/BUNDLE_SPEC.md) exist.

**References:** 

- <https://github.com/oras-project/artifacts-spec/blob/main/manifest-referrers-api.md>
- <https://github.com/sigstore/cosign/blob/main/specs/BUNDLE_SPEC.md> 
- <https://github.com/sigstore/cosign/blob/main/specs/SIGNATURE_SPEC.md>
- <https://github.com/sigstore/cosign>