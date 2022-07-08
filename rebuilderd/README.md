# rebuilderd

rebuilderd is a build system project part of Reproducible Builds. Each instance
of rebuilderd compiles source code for built artifacts in a similar environment
as the original to check if the build process is reproducible. The system
currently has support for Arch Linux, Debian, and Tails, with support for
Alpine planned.

When the result of a rebuild is positive, i.e., the build process is found to
be reproducible, rebuilderd generates an in-toto link recording this result.
This link metadata can be fetched from a cluster of rebuilderd instances to
verify that multiple, independent instances attested to the reproducibility
of a package prior to its use.

## References

* https://rebuilderd.com/
* https://github.com/kpcyrd/rebuilderd
* https://r-b.engineering.nyu.edu/
* https://reproducible.seal.purdue.wtf/