# Datadog

Datadog uses in-toto to secure its agent integrations as they move through the
company's CI/CD system. Datadog's developers sign an in-toto link for a tag
they want to release which then moves through the CI/CD system. This system is
responsible for building Python wheels and generates in-toto link metadata as
well. All of this metadata is verified by the Datadog agent running on customer
hardware, guaranteeing the integrity of the CI/CD system.

Interestingly, Datadog combined in-toto with its sister project, The Update
Framework (TUF). TUF is used to securely deliver both the agent integrations
and the in-toto metadata--in a sense, TUF is used to bootstrap trust for the
in-toto layout as well. The combination of in-toto and TUF is detailed in two
ITEs, ITE-2 and ITE-3.

## References

* https://www.datadoghq.com/blog/engineering/secure-publication-of-datadog-agent-integrations-with-tuf-and-in-toto/
* https://github.com/in-toto/ITE/blob/master/ITE/2/README.adoc
* https://github.com/in-toto/ITE/blob/master/ITE/3/README.adoc