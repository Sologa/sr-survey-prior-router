# lens_api (official_scholarly_examples)

Source URL: https://docs.api.lens.org/examples-scholar.html
Local raw file: `references/canonical_sources/raw/lens_api/official_scholarly_examples_examples-scholar.html.html`

Scholar Examples

- Home

- Getting Started

- Getting Started

- Support

- Request

- Scholar Request

- Patent Request

- Response

- Scholar Response

- Patent Response

- Aggregations

- Examples

- Scholar Examples

- Patent Examples

- Scholar Code Samples

- Patent Code Samples

- Bulk Data

#### Table of Contents

- Find 20 records

- Get the patent citations

- Get works using a `doi`

- Using multiple pmid

- Cited by patent lens_id

- 10 most recently published works

- Publication year of articles cited by patents

- 30 works published between two years

- Works having patent citations and affiliations

- Query by author name

- Pubmed identifier published in 2012

- Access your collection

- Using GET Requests

### Contact Support

To report any bugs, issues and usability of APIs or for general questions or to provide feedback, please visit support.
Visit Support

# Scholar Examples

##### Find 20 records from offset 10 that match provided query

{ "query" : "X-ray analysis of protein crystals" , "size" : 20 , "from" : 10 }

##### Get the patent citations, scholarly citations and references for a list of scholarly works using the lens_id

{ "query" : { "terms" :{ "lens_id" : [ "017-767-306-508-482" , "017-624-265-921-255" ] } }, "include" : [ "lens_id" , "patent_citations" , "scholarly_citations" , "references" ] }

##### Get title and patent citations for a scholarly work using a doi

{ "query" : { "match" :{ "doi" : "10.1109/ee.1934.6540358" } }, "include" :[ "title" , "patent_citations" ] }

##### Get scholarly works using multiple pmid

{ "query" : { "terms" : { "pmid" : [ "14297189" , "17475107" ] } } }

##### Get the metadata for scholarly works that are cited by a list of patents using the patent lens_id

{ "query" : { "terms" : { "patent_citation.lens_id" :[ "198-832-374-467-397" , "092-513-162-449-806" ] } } }

##### Find the 10 most recently published works from an institution (sorted by published date)

{ "query" : { "match_phrase" : { "author.affiliation.name" : "Harvard University" }}, "sort" : [{ "date_published" : "desc" }], "size" : 10 }

##### Get publication year of journal articles cited by patents

{ "query" : { "bool" : { "must" : [ { "terms" : { "patent_citation.lens_id" : [ "020-159-299-402-960" , "014-680-767-794-441" ]}}, { "match" : { "source.type" : "Journal" }} ] } }, "include" : [ "year_published" ], "size" : 50 }

##### Get 30 works from an institution published between two years

{ "query" : { "bool" : { "must" : { "match_phrase" : { "author.affiliation.name" : "Harvard University" }}, "filter" : { "range" : { "year_published" : { "gte" : "1999" , "lte" : "2000" } } } } }, "size" : 30 }

##### Get scholarly works having patent citations and affiliations

{ "query" : { "bool" :{ "must" : [ { "match" : { "has_patent_citations" : true }}, { "match" : { "has_affiliation" : true }} ] } } }

##### Query by author name

{ "query" : { "match_phrase" : { "author.display_name" : "Craig Venter" } }, "sort" : [{ "year_published" : "desc" }], "size" : 10 }

##### Find scholarly works with a Pubmed identifier published in 2012

{ "query" : { "bool" :{ "must" :[ { "match" :{ "external_id_type" : "pmid" }}, { "match" :{ "year_published" : 2012 }} ] } }, "include" :[ "patent_citations_count" , "external_ids" ] }

OR using String Based Query

{ "query" : "external_id_type: pmid AND year_published: 2012" , "include" :[ "patent_citations_count" , "external_ids" ] }

##### Access your collection

[POST] https://api.lens.org/collections/123456

{ "query" : { "match" : { "title" : "Malaria" }}, "include" :[ "title" , "lens_id" , "authors.first_name" ], "size" : 10 }

##### Using GET Requests

[GET] https://api.lens.org/collections/123456?token=[your-access-token]&size=10&query=Malaria&include=authors,lens_id&sort=desc(date_published)

[GET] https://api.lens.org/scholarly/search?token=[your-access-token]&size=10&query=Malaria&include=authors,lens_id&sort=desc(date_published)

Copyright © 2024
