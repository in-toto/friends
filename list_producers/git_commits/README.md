---
type: Repository
besides: Yes
format: [Any (Suggested Attestation Bundle)]
visibility: [Public, Private]
---

# Git Commits

Git Commits can have [Git Notes](https://git-scm.com/docs/git-notes) associated with attestations. Tools such as [`gitsign`](https://github.com/sigstore/gitsign), [`slsa-source-tool`](https://github.com/slsa-framework/source-tool), and [`gittuf`](https://github.com/gittuf/gittuf) store attestations in this way. There are current efforts underway to standardize the naming of the Git Notes to `refs/attestations/<type>`. Although to find the current naming convention for each repository, one can use `git ls-remote <repository_name> | grep -vE 'refs/(heads|tags|pull)'`   (or similar) to find the referenced sha and get the associated commit.

**References:** 

- <https://github.com/in-toto/ITE/pull/61>