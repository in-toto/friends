---
type: Database
besides: No
format: [dsse, intoto, hashedrekord]
visibility: [Public, Private]
---


# Sigstore Rekor

[Sigstore Rekor](https://www.sigstore.dev/) provides an immutable tamper-resistant ledger of software supply chain metadata. For older `in-toto` entries, Rekor stores the attestation payload and certificate, whereas newer entries (e.g., `dsse` and `hashedrekord`) do not. A public instance of Sigstore Rekor is available, while organizations can also create private instances.

**References:** 

- <https://github.com/sigstore/rekor>
- <https://docs.sigstore.dev/logging/overview/>