# ieee_xplore_api (official_metadata_api_responses)

Source URL: https://developer.ieee.org/docs/read/Metadata_API_responses
Local raw file: `references/canonical_sources/raw/ieee_xplore_api/official_metadata_api_responses_metadata_api_responses.html`

IEEE Xplore - Data Fields Returned

IEEE Xplore

- [Sign In](https://developer.ieee.org/login/login?r=https%3A%2F%2Fdeveloper.ieee.org%2Fdocs%2Fread%2FMetadata_API_responses&h=aa62b713e86dd44e15adac6501baf541)

- [Register](https://developer.ieee.org/member/register)

- Previous: [Boolean Search Operators](https://developer.ieee.org/docs/read/metadata_api_details/Leveraging_Boolean_Logic)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [API Use Case Examples](https://developer.ieee.org/docs/read/API_Use_Cases_Examples)

# Data Fields Returned

The table below lists available metadata fields. Only populated fields will be returned so content may differ by publication.

Data Field

Description

abstract

Brief summary or statement of the contents of a journal article, conference paper, standard, book / book chapter, and/or course.

abstract_url

IEEE Xplore URL that will return the abstract.

author_url

IEEE Xplore URL that returns the author details. For more information please go to: https://ieeexplore.ieee.org/Xplorehelp/#/author-center/author-details

accessType

accessType key:

NOTE: The returned metadata will identify each response with access type. All available full-text articles (Ex: Open Access, etc.) must be requested by a subsequent URL including the article number. Ex:http://ieeexploreapi.ieee.org/api/v1/search/document/6762843/fulltext?apikey=[Customer API Key here]&format=xml

'Open Access' - Freely available from IEEE.

'Ephemera' - Freely available from IEEE.

'Locked'- Sign in or learn about subscription options.

'Plagarized'- Marked as a plagarized article.

article_number

IEEE’s unique identifier for a specific article.

author_order

Where multiple authors are listed, the author_order provides a number for each author.

author_terms

Terms provided by the author which describe the topics or subjects of the document.

authors

Name of the author(s) listed in the document. Author names are provided as full names along with their listed order.

affiliation

Name of the affiliation(s) listed in the document. Affiliation names are provided as full names along with their listed order.

citing_paper_count

Number of papers citing the given article.

citing_patent_count

Number of patents citing the given article.

conference_dates

Date of conference event. Date format is not standardized and varies by conference.

conference_location

Location of conference event (can be one or more city, state, country).

content_type

Specifies what kind of publication the content is from. Content type can include:

Books / ebooks

Conferences

Courses

Early Access

Journals

Magazines

Standards

start-record

A place holder within the delivery for multiple interactions searching large volumes of data. Note: The number of maximum results is 200. The start-record field is used to iterate through additional results as appropriate. The Dynamic Query Tool and SDKs outline its use.

d-au

Open Author Facet

doi

The Digital Object Identifier (doi) is the unique identifier assigned to an article / document by CrossRef.

d-publisher

Open Publisher's Facet

d-pubtype

Open Content Type Facet

d-year

Open Publication Facet

end_page

The final page number in the print version of the article.

facet

Open/Facet dimension

full_name

The full name of an author.

html_url

IEEE Xplore URL that will return the full-text HTML.

ieee_terms

Keywords assigned to IEEE journal articles and conference papers from a controlled vocabulary created by the IEEE.

index_terms

This is a combined field which returns Author Keywords and IEEE Terms.

insert_date

Date of last update (yyyymmdd).

is_number

Internal issue identifier (Journals only)

isbn

International Standard Book Number. A number used to uniquely identify a book or non-serial.

issn

International Standard Serial Number. An 8-digit number used to uniquely identify a periodical publication (journal or serial).

issue

Number of the journal issue in which the article was published.

pdf_url

IEEE Xplore URL that returns the full-text pdf.

publication_date

Date the article was published; this data can be represented as full date, month and year, or quarter and year. Format varies by publication.

publication_year

Year the article was published; this data can be represented as full date, month and year, or quarter and year. Format varies by publication.

publication_number

A unique IEEE record number assigned to a publication.

publication_title

Title of a publication (journal, conference, book / ebook, standard, course).

publisher

Name of Publisher for the specific publication referenced.

rank

Rank indicates the hierarchy of the returned documents based on an IEEE algorithm used.

standard_number

Standard designation (e.g., IEEE 802.11u-2011). Standard designations are allocated by the Administrator of the IEEE-SA Standards Board New Standards Committee (NesCom).

standard_status

Status of standard (e.g. Active, Draft, etc.); applies only to Standards.

start_page

Starting page number on print version of article.

title

Title of an individual document (journal article, conference paper, standard, Book / eBook chapter or Course)

totalfound

Total number of documents found that match the query criteria.

totalsearched

Total number of documents searched.

volume

Detail associated with Journals and Conferences only.

version 42 as of 2 years ago by Manny Rechani

- Previous: [Boolean Search Operators](https://developer.ieee.org/docs/read/metadata_api_details/Leveraging_Boolean_Logic)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [API Use Case Examples](https://developer.ieee.org/docs/read/API_Use_Cases_Examples)

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
