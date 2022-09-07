# SLSA

Supply chain Levels for Software Artifacts, or SLSA, is a framework that
provides a series of requirements and controls. These requirements are
divided across four levels with SLSA Level 1 providing the least guarantees
and SLSA Level 4 providing the highest assurances.

The lowest tier, SLSA Level 1, requires provenance information to be generated
for a software artifact, with the SLSA provenance specification written as an
in-toto attestation. Another type is the Verification Summary Attestation, that
communicates an artifact has been verified at a particular SLSA level. Both of
these are generated via the in-toto attestation framework.

## References

* https://slsa.dev/provenance/v0.2
* https://slsa.dev/verification_summary/v0.1
* https://github.com/in-toto/attestation