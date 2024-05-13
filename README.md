# in-toto/friends

This repository is a place to record integrations (ongoing and complete) and adoptions of in-toto. This information can be useful to sharing the nuances of specific integrations or adoptions which can help newer adopters in the future.

We welcome adopters to add to the list here by creating a directory with a README file describing how they use in-toto. The directory can contain any other artifacts necessary to detail the in-toto integration.


## Project Adopters
This section lists organizations or individuals who have adopted the project and are using it in their workflows or systems. These adopters contribute to the project's ecosystem and showcase its real-world usage across various domains.

| Adopter Name  | logo | Description |
|---------------|------|-------------|
| Datadog       |<img src="https://imgix.datadoghq.com/img/about/presskit/logo-v/dd_vertical_white.png" width="50" height="50">|Datadog uses in-toto to secure its agent integrations as they move through the company's CI/CD system. |
| OpenVEX       |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/684de18e-db0c-4b2a-bc35-a6e7b86102ea" width="50" height="50">|OpenVEX documents are designed to be self-sustaining, but the specification is designed to benefit from the in-toto attestation format completing VEX statements with data outside of the OpenVEX predicate. |
| SLSA          |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/4b5b5c88-2f54-4635-9f32-18f9ac1bc944" width="50" height="50">|Supply chain Levels for Software Artifacts, or SLSA, is a framework that provides a series of requirements and controls. |
| SolarWinds    |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/dec6a636-459b-42c7-b106-55be1ee16e9c" width="50" height="50">       |SolarWinds is an American company that provides information technology services and software to other companies and government agencies. |


## Project Integrations
This section lists software systems, services, or platforms that integrate with the project to provide additional functionality, interoperability, or compatibility. These integrations enhance the project's capabilities and extend its usefulness across various ecosystems.

| Integration Name | Logo | Description |
|------------------|------|-------------|
| GitLab           | <img src="https://github.com/DarikshaAnsari/friends/assets/100822529/6a01cb62-19ce-469c-af85-cee0688146e9" width="50" height="50">| GitLab is a popular Git server that also provides CI/CD integrations. |
| Grafeas          |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/3a9654d1-8a28-4c12-8ff3-90ffc5fddcbb" width="50" height="50">| Grafeas is an open source metadata API that is used to store metadata relevant to software supply chains. Grafeas includes support for in-toto link metadata. |
| GUAC             |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/4e3bee40-55e7-49c9-b32c-95c78ef0ed1a" width="50" height="50">| GUAC has the ability to ingest and parse SLSA and other in-toto ITE6 attestations (either wrapped in DSSE or standalone). |
| Hoppr            || Hoppr leverages the in-toto python package to generate in-toto layout files based on a hoppr transfer configuration. |
| Jenkins          |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/ea75ad14-7b16-4e02-8429-d31ea842390b" width="50" height="50">| The in-toto team maintains a plugin for Jenkins that can be used to generate in-toto metadata pertaining to a particular build or "job". |
| rebuilderd       || Rebuilderd is a build system project part of Reproducible Builds. When the result of a rebuild is positive, i.e., the build process is found to be reproducible, rebuilderd generates an in-toto link recording this result. |
| Sigstore         |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/874fb768-2e01-40df-bc7f-9b10f08339b5" width="50" height="50">| In-toto and Sigstore are complementary in their efforts, and Sigstore integrates in-toto in a number of ways. Sigstore's keyless signing can be used to sign in-toto metadata, as demonstrated by Cosign's SLSA Provenance generation. |
| Tekton Chains    | <img src="https://github.com/DarikshaAnsari/friends/assets/100822529/e71898e5-42b9-4560-b90a-df40fbcfe52a" width="50" height="50">| Tekton Chains is a component for Tekton that adds software supply chain security. Chains observes all "TaskRuns" or jobs that are executed, and generates an in-toto attestation. |
| TestifySec       |<img src="https://github.com/DarikshaAnsari/friends/assets/100822529/49b737a4-b3bc-495d-a7f5-22b87fbc697a" width="50" height="50">| TestifySec is a software supply chain security company that has created two open source projects that leverage in-toto. Witness and Archivista. |


## Credit

The `friends` idea was borrowed from other communities in the space like Sigstore and tektoncd.
