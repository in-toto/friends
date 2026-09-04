---
type: Images
besides: Either
format: [Attestation Blob]
visibility: [Public, Private]
---

# Attestation Manifest

If [Buildkit](https://github.com/moby/buildkit) is used for images, attestations are stored within the manifest objects annotated as `"vnd.docker.reference.type": "attestation-manifest"`.

**References:** 

- <https://github.com/moby/buildkit/blob/master/docs/attestations/attestation-storage.md>
- <https://docs.docker.com/dhi/how-to/verify/>
- <https://github.com/docker/scout-cli>
- <https://docs.docker.com/build/metadata/attestations/attestation-storage>