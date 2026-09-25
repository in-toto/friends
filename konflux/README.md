# Konflux

The Konflux platform is an open source, cloud native software factory focused
on supply chain security.

It produces in-toto attestations from the control plane with [Tekton
Chains](../tekton-chains/README.md) and it uses those attestations to gate
artifacts with machine-readable policies with
[Conforma](../conforma/README.md). Those attestations and policy verification
form the basis of a trust chain used to establish trust other aspects of the
build process, like the software bill of materials (SBOM) created as a
byproduct of offline hermetic builds.

## References

* https://konflux-ci.dev/
* https://konflux-ci.dev/docs/metadata/
