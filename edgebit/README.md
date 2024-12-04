# EdgeBit

[EdgeBit](https://edgebit.io) is a software supply chain security platform that has created [SBOM server](https://github.com/edgebitio/sbom-server), an SBOM and in-toto generator that is [anchored in a hardware root-of-trust through an AWS Nitro Enclave](https://edgebit.io/blog/generating-sboms-with-a-hardware-root-of-trust/).

SBOM server is an experiment in SBOM authenticity and remote SBOM (and in-toto) generation. When a remote container image is streamed into the server, an [in-toto attestation bundle][bundle] containing the following attestations is returned:

- [SLSA Provenance][provenance] - indicates the versions of the server and
  external tools, as well as the initial arguments to the server
- [SCAI Attribute Report][scai] - contains the enclave attestation document
  which proves the enclave image and the public key for the signatures on the
  other attestations in the bundle
- [SPDX Document][spdx] - contains the SPDX-formatted SBOM generated from the
  provided artifact

The entire document is rooted in AWS' Nitro Attestation PKI.

[bundle]: https://github.com/in-toto/attestation/blob/v1.0/spec/v1.0/bundle.md
[provenance]: https://slsa.dev/spec/v1.0/provenance
[scai]: https://github.com/in-toto/attestation/blob/v1.0/spec/predicates/scai.md
[spdx]: https://github.com/in-toto/attestation/blob/v1.0/spec/predicates/spdx.md
