# Sigstore

[Sigstore](https://sigstore.dev) is a set of software supply chain security
tools that handles cryptographic signing, verification using short-lived keys.
In addition, Sigstore supports verifying the provenance of signed software.

in-toto and Sigstore are complementary in their efforts, and Sigstore integrates
in-toto in a number of ways. Sigstore's keyless signing can be used to sign
in-toto metadata, as demonstrated by Cosign's [SLSA](/slsa/README.md) Provenance
generation. In addition, Rekor, Sigstore's transparency log, can be used to
record in-toto attestations in its immutable store. Finally, using semantics
described in [in-toto Enhancement 7](https://github.com/in-toto/ITE/blob/master/ITE/7/README.adoc),
in-toto layouts can verify Sigstore signatures natively.
