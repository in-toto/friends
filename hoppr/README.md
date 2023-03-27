# Hoppr

Hoppr is an open source software bill-of-materials (SBOM) and secure software
supply-chain (S3C) utility kit. Built on a simple plugin architecture, Hoppr
can collect, process, and bundle digital assets to streamline transfers
from one production environment to another. Whether on cloud-connected or
airgapped networks, Hoppr can handle it.

Hoppr leverages the `in-toto` python package to generate in-toto layout
files based on a hoppr transfer configuration. in-toto links are generated
for each stage of processing in Hoppr. Future work includes collection of
SBOM component attestations from Archivista.

## References

* https://hoppr.dev/
* https://gitlab.com/hoppr/hoppr/-/blob/dev/hoppr/in_toto.py