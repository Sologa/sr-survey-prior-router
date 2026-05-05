# ieee_xplore_api (official_metadata_api_details)

Source URL: https://developer.ieee.org/docs/read/Metadata_API_details
Local raw file: `references/canonical_sources/raw/ieee_xplore_api/official_metadata_api_details_metadata_api_details.html`

IEEE Xplore - Search Parameters

IEEE Xplore

- [Sign In](https://developer.ieee.org/login/login?r=https%3A%2F%2Fdeveloper.ieee.org%2Fdocs%2Fread%2FMetadata_API_details&h=ef9d162eceaa9526ede6e3c65914dbca)

- [Register](https://developer.ieee.org/member/register)

- Previous: [API Query Basics](https://developer.ieee.org/docs/read/Searching_the_IEEE_Xplore_Metadata_API)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [Filtering Parameters](https://developer.ieee.org/docs/read/metadata_api_details/Filtering_Parameters)

# Search Parameters

Parameter

Description

abstract

Brief summary or statement of the contents of a journal article, conference paper, standard, book, book chapter, or course.

affiliation

This field is used to submit a query that specifies part (min of 3 characters) or all of an organization/institution name and receive a response of all available metadata with articles authored by an individual(s) associated with that organization/institution.

article_number

This is IEEE’s unique identifier for a specific article.

Please note: this parameter can only be used by itself. If used with other parameters, all other parameters are ignored.

article_title

Title of an individual document (journal article, conference paper, standard, eBook chapter, or course).

author

An author's name. Searches both first name and last name. A minimum of 3 characters preceding the wildcard (*) is required.

d-au

Open Author facet; results contain a refinement link that returns all documents by a given author relevant to that search.

doi

The Digital Object Identifier (doi) is the unique identifier assigned to an article / document by CrossRef. If included, all other parameters are ignored with the exception of article_number , which still overrides all other search parameters.

d-publisher

Publisher facet; results contain a refinement link that returns all documents by a given publisher relevant to that search.

d-pubtype

Content Type facet; results contain a refinement link that returns all documents by a given content type relevant to that search.

d-year

Publication Year facet

end_date

This field will allow customers to query on month and date of insertion. This will enable customers to run a delta update using month and year. Metadata API for insert date will include: -To (Insert) Date (YYYYMMDD)

facet

Open/Facet dimension

index_terms

This is a combined field which allows users to search the Author Keywords, IEEE Terms, and Mesh Terms.

Please note: this parameter should contain no more than two wildcard words. Each wildcard word must have a minimum of three characters preceding the wildcard (*).

isbn

International Standard Book Number. A number used to uniquely identify a book or non-serial.

issn

International Standard Serial Number. An 8-digit number used to uniquely identify a periodical publication (journal or serial).

is_number

Issue number (for Journals only)

meta_data

This field enables a free-text search of all configured metadata fields and the abstract . Accepts complex queries involving field names and boolean operators.

Please note: this parameter should contain no more than two wildcard words. Each wildcard word must have a minimum of three characters preceding the wildcard (*).

publication_id

Publication Id search parameter.

publication_title

Title of a publication (Journal, Conference, or Standard).

publication_year

The value for publication year varies by publication. It is recommended to verify the format of the particular publication within the Xplore Web product to learn how to structure your search query.

querytext

This field enables a free-text search of all configured metadata fields and abstract text . Accepts complex queries involving field names and boolean operators .

Please note: this parameter should contain no more than two wildcard words. Each wildcard word must have a minimum of three characters preceding the wildcard (*).

start_date

This field will allow customers to query on month and date of insertion. This will enable customers to run a delta update using month and year. Metadata API for insert date will include: -From (Insert) Date (YYYYMMDD)

start_record

A place holder within the delivery for multiple interactions searching large volumes of data. Note: The number of maximum results is 200. The start-record field is also used to iterate through additional results as appropriate. The Dynamic Query Tool and SDKs outline its use.

thesaurus_terms

Also referred to as IEEE Terms. These are keywords assigned to IEEE journal articles and conference papers from a controlled vocabulary created by the IEEE.

Please note: this parameter should contain no more than two wildcard words. Each wildcard word must have a minimum of three characters preceding the wildcard (*).

version 63 as of 2 years ago by Manny Rechani

- Previous: [API Query Basics](https://developer.ieee.org/docs/read/Searching_the_IEEE_Xplore_Metadata_API)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [Filtering Parameters](https://developer.ieee.org/docs/read/metadata_api_details/Filtering_Parameters)

## Docs Navigation

- [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- [API Use Cases](https://developer.ieee.org/docs/read/IEEE_Xplore_Metadata_API_Overview)

- [API Query Basics](https://developer.ieee.org/docs/read/Searching_the_IEEE_Xplore_Metadata_API)

- [Search Parameters](https://developer.ieee.org/docs/read/Metadata_API_details)

- [Filtering Parameters](https://developer.ieee.org/docs/read/metadata_api_details/Filtering_Parameters)

- [Sorting and Paging Parameters](https://developer.ieee.org/docs/read/metadata_api_details/Sorting_and_Paging_Parameters)

- [Boolean Search Operators](https://developer.ieee.org/docs/read/metadata_api_details/Leveraging_Boolean_Logic)

- [Data Fields Returned](https://developer.ieee.org/docs/read/Metadata_API_responses)

- [API Use Case Examples](https://developer.ieee.org/docs/read/API_Use_Cases_Examples)

- [Getting Started](https://developer.ieee.org/Quick_Start_Guide)

- [Dynamic Query Tool](https://developer.ieee.org/Dynamic_Query_Tool)

- [Documentation](https://developer.ieee.org/docs)

- [SDKs](https://developer.ieee.org/PHP_Software_Development_Kit)

- [Contact Us](https://developer.ieee.org/contact)

- [Terms of Use](https://developer.ieee.org/API_Terms_of_Use2)

- [IEEE.org](http://ieeexplore.ieee.org)

- [Contact Us](https://developer.ieee.org/contact)

- [Terms of Use](https://developer.ieee.org/API_Terms_of_Use2)

- [IEEE.org](http://ieeexplore.ieee.org)

Copyright IEEE - All rights reserved.
