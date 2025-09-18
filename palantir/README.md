# Palantir (Project Adopter)

Palantir uses in-toto to protect the integrity of software from source to deployment across a large, heterogeneous environment.

## Highlights
- **Multi-ecosystem builds:** Custom tooling emits signed attestations across Gradle, Godel, containers, Helm, and frontend bundles.
- **Verifiable provenance:** Release and build steps produce attestations binding source commits/tags to produced artifacts.
- **Enterprise distribution:** Attestations are packaged with artifacts and stored in existing artifact repositories, supporting disconnected/offline installs.
- **Layered verification:** Verification occurs at publication and again at install time to guard against tampering in transit.
- **Operational rollout:** Gradual enforcement with exemptions and controlled overrides ensured continuity for mission-critical services.
- **Spec alignment:** Migration to in-toto v1 (with SLSA build attestations) simplified verification and improved performance at scale (e.g., reducing P99 verification spikes from ~90 minutes to <15).

## Reference
“[How Palantir Mastered In-Toto](https://blog.palantir.com/how-palantir-mastered-in-toto-b8a7107371bb)” (Medium, Sep 2025).
