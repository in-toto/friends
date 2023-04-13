# GUAC: Graph for Understanding Artifact Composition

Graph for Understanding Artifact Composition (GUAC) aggregates software security metadata into a high fidelity graph database—normalizing entity identities and mapping standard relationships between them. Querying this graph can drive higher-level organizational outcomes such as audit, policy, risk management, and even developer assistance.

GUAC has the ability to ingest and parse SLSA and other in-toto [ITE6 attestations](https://github.com/in-toto/attestation) (either wrapped in [DSSE](https://github.com/secure-systems-lab/dsse) or standalone). Combining this attestation and identity information data with other information obtain about the artifact being attested, allows for in-depth understanding into the software supply chain. This aggregation of data can be used to quickly make audit, policy and risk management decisions.

## References

* <https://github.com/guacsec/guac>
