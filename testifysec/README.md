# TestifySec

TestifySec is a supply chain security company that has created two open source projects that leverage `in-toto`. 

## Witness
[Witness](https://github.com/testifysec/witness/#key-features) contains partial implementation of the in-toto specification including ITE-5, ITE-6, and ITE-7, and an embedded rego policy engine for build policy enforcement (which will align with ITE-10 in the future).

## Archivista
[Archivista](https://github.com/testifysec/archivista#archivista) is a graph and storage service for `in-toto` attestations. It allows the querying of metadata via a GraphQL API.