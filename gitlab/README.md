# GitLab

GitLab is a popular Git server that also provides CI/CD integrations. GitLab
Runner, the component that runs jobs in the CI/CD system, is being updated to
achieve [SLSA](../slsa/README.md) compliance. Therefore, work is underway to
generate SLSA provenance in-toto attestations.

## References

* https://docs.gitlab.com/ee/ci/runners/configure_runners.html#artifact-attestation
* https://gitlab.com/gitlab-org/gitlab-runner/-/issues/28217
