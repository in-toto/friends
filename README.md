# in-toto/friends

This repository is a place to record integrations (ongoing and complete) and adoptions of in-toto. This information can be useful to sharing the nuances of specific integrations or adoptions which can help newer adopters in the future.

We welcome adopters to add to the list here by creating a directory with a README file describing how they use in-toto. The directory can contain any other artifacts necessary to detail the in-toto integration.


## Project Adopters
This section lists organizations or individuals who have adopted the project and are using it in their workflows or systems. These adopters contribute to the project's ecosystem and showcase its real-world usage across various domains.

| Adopter Name  | logo | Description |
|---------------|------|-------------|
| Datadog       |<img src="img/Adopters_logo/Datadog_logo.png" width="50" height="50">|Datadog uses in-toto to secure its agent integrations as they move through the company's CI/CD system. |
| OpenVEX       |<img src="img/Adopters_logo/OpenVEX_logo.png" width="50" height="50">|OpenVEX documents are designed to be self-sustaining, but the specification is designed to benefit from the in-toto attestation format completing VEX statements with data outside of the OpenVEX predicate. |
| SLSA          |<img src="img/Adopters_logo/SLSA_logo.svg" width="50" height="50">|Supply chain Levels for Software Artifacts, or SLSA, is a framework that provides a series of requirements and controls. |
| SolarWinds    |<img src="img/Adopters_logo/Solarwinds_Logo.png" width="50" height="50">|SolarWinds is an American company that provides information technology services and software to other companies and government agencies. |


## Project Integrations
This section lists software systems, services, or platforms that integrate with the project to provide additional functionality, interoperability, or compatibility. These integrations enhance the project's capabilities and extend its usefulness across various ecosystems.

| Integration Name | Logo | Description |
|------------------|------|-------------|
| GitHub           | <img src="img/Integrations_logo/GitHub_logo.png" width="50" height="50">| GitHub is a developer platform popular across enterprises and open source. GitHub artifact attestations supports SLSA build provenance and SBOM in-toto predicate types. |
| GitLab           | <img src="img/Integrations_logo/Gitlab_logo.png" width="50" height="50">| GitLab is a popular Git server that also provides CI/CD integrations. |
| Grafeas          |<img src="img/Integrations_logo/Grafeas_logo.png" width="50" height="50">| Grafeas is an open source metadata API that is used to store metadata relevant to software supply chains. Grafeas includes support for in-toto link metadata. |
| GUAC             |<img src="img/Integrations_logo/Guac_logo.png" width="50" height="50">| GUAC has the ability to ingest and parse SLSA and other in-toto ITE6 attestations (either wrapped in DSSE or standalone). |
| Hoppr            || Hoppr leverages the in-toto python package to generate in-toto layout files based on a hoppr transfer configuration. |
| Jenkins          |<img src="img/Integrations_logo/Jenkins_logo.png" width="50" height="50">| The in-toto team maintains a plugin for Jenkins that can be used to generate in-toto metadata pertaining to a particular build or "job". |
| rebuilderd       || Rebuilderd is a build system project part of Reproducible Builds. When the result of a rebuild is positive, i.e., the build process is found to be reproducible, rebuilderd generates an in-toto link recording this result. |
| Sigstore         |<img src="img/Integrations_logo/Sistore_logo.png" width="50" height="50">| In-toto and Sigstore are complementary in their efforts, and Sigstore integrates in-toto in a number of ways. Sigstore's keyless signing can be used to sign in-toto metadata, as demonstrated by Cosign's SLSA Provenance generation. |
| Tekton Chains    | <img src="img/Integrations_logo/Tekton_logo.png" width="50" height="50">| Tekton Chains is a component for Tekton that adds software supply chain security. Chains observes all "TaskRuns" or jobs that are executed, and generates an in-toto attestation. |
| TestifySec       |<img src="img/Integrations_logo/Testifysec_logo.svg" width="50" height="50">| TestifySec is a software supply chain security company that has created two open source projects that leverage in-toto. Witness and Archivista. |


## Credit

The `friends` idea was borrowed from other communities in the space like Sigstore and tektoncd.
