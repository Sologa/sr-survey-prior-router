# Europe PMC REST and bulk services

Source URL: https://europepmc.org/RestfulWebService
Local raw file: `/Volumes/My Book/NLP_PRISMA_Reviews/docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/europe_pmc/canonical_restfulwebservice.html`

Europe PMC Europe PMC RESTful Web Service - Developers - Europe PMC
1

Sign in | Create an account https://orcid.org https://plus.europepmc.org

-
Europe PMC
Menu

- About

- About Europe PMC

- Preprints in Europe PMC

- Funders

- Become a funder

- Governance

- Roadmap

- Outreach

- Tools

- Tools overview

- Article status monitor

- Grant finder

- External links service

- RSS feeds

- About SciLite annotations

- Annotations submission service

- Developers

- Developer resources

- Articles RESTful API

- Grants RESTful API

- API case studies

- SOAP web service

- Annotations API

- OAI service

- Bulk downloads

- [Developers Forum](http://groups.google.com/a/ebi.ac.uk/forum/#!forum/epmc-webservices)

- Support

- User guide

- Search syntax guide

- Contact us

- Contact us

- Helpdesk

- Feedback

- [Twitter](https://twitter.com/EuropePMC_news)

- [Blog](http://blog.europepmc.org)

- Tech blog

- Developer Forum

- [Europe PMC plus](https://plus.europepmc.org/)

# Search life-sciences literature (47,904,215 articles, preprints and more)

Search
Advanced search | Recent history

Feedback Complete Survey Survey

This website requires cookies, and the limited processing of your personal data in order to function. By using the site you are agreeing to this as outlined in our privacy notice and cookie policy .

# Search life-sciences literature (47,904,215 articles, preprints and more)

Search
Advanced search | Recent history

Feedback Complete Survey Survey

This website requires cookies, and the limited processing of your personal data in order to function. By using the site you are agreeing to this as outlined in our privacy notice and cookie policy .

# Articles RESTful API

Use API functionality to [access the latest articles and preprints on the Coronavirus programatically](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%222019-nCoV%22%20OR%20%222019nCoV%22%20OR%20%22COVID-19%22%20OR%20%22SARS-CoV-2%22%20OR%20(%22wuhan%22%20AND%20%22coronavirus%22)%20OR%20%22Coronavirus%22%20OR%20%22Corona%20virus%22%20OR%20%22corona-virus%22%20OR%20%22corona%20viruses%22%20OR%20%22coronaviruses%22%20OR%20%22SARS-CoV%22%20OR%20%22Orthocoronavirinae%22%20OR%20%22MERS-CoV%22%20OR%20%22Severe%20Acute%20Respiratory%20Syndrome%22%20OR%20%22Middle%20East%20Respiratory%20Syndrome%22%20OR%20(%22SARS%22%20AND%20%22virus%22)%20OR%20%22soluble%20ACE2%22%20OR%20(%22ACE2%22%20AND%20%22virus%22)%20OR%20(%22ARDS%22%20AND%20%22virus%22)%20OR%20(%22angiotensin-converting%20enzyme%202%22%20AND%20%22virus%22)&resultType=core) .

## RESTful Web Service

1. Quick Start

2. Web Service Overview

3. Web Service Releases

4. Sorting Results

5. Result Types

6. Request Methods

7. Release Notes

8. Privacy Notice

## Quick Start

For a quick start, click on the following link (opens in new window):

[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=p53](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=p53)
Come back to this page for further guidance and help.

## Web Service Overview

The Europe PMC RESTful Web Service gives you access to over 33 million publications from various sources, including PubMed, Agricola, the European Patents Office (EPO) and the National Institute for Clinical Excellence (NICE). Use the Web Service to access

- 10.2 million full text articles and 6.5 million open access articles

- Database cross-references to a number of databases, including UniProt, the European Nucleotide Archive (ENA) and more.

- Reference lists for more than 19.4 million publications.

- Citation counts and a citation network.

- Text-mined terms from full text articles, including accession numbers, chemicals, diseases, genes and proteins, Gene Ontology terms, and organisms. Use the Annotations API to access annotations in abstracts and full text articles, with links to related database records.

For background information on Europe PMC content refer to the Web Service Reference Guide (Sections 2 and 3) and What am I searching on Europe PMC?

The search module can be used to query search fields. Refer to the fields module, the search syntax reference or the Web Service Reference Guide for a list of available fields.

Output response formats can be XML or JSON. In the case of the 'search' module a Dublin Core format is also available.

## Web Service Releases

Two versions of the RESTful web service are simultaneously available. This approach to release management allows users to prepare for a new version, rather than having to immediately respond to a version change. Join the [Europe PMC web service users' Google group](https://groups.google.com/a/ebi.ac.uk/forum/#!forum/epmc-webservices) to receive notifications about web service releases.

Construct your URL for a fields request as follows for the production version:
GET [https://www.ebi.ac.uk/europepmc/webservices/rest/fields](https://www.ebi.ac.uk/europepmc/webservices/rest/fields)
Construct your URL for a fields request as follows for the test version of the web service:
GET [https://www.ebi.ac.uk/europepmc/webservices/test/rest/fields](https://www.ebi.ac.uk/europepmc/webservices/test/rest/fields)
See the latest release notes .

## Sorting Results

By default, the Europe PMC RESTful search results are sorted by relevance, with the most relevant result being presented first in the list.

The search module additionally provides a sort parameter available for every single-valued field, e.g. P_PDATE_D, AUTH_FIRST, CITED. The sort parameter can be combined with'asc' or 'desc' sort order.

RESTful search results can be sorted in two other ways using the arguments: 'sort_date:y' and 'sort_cited:y' in the 'query' parameter of the search module. For example:

Sort by the number of citations, most cited being the first result presented:
[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria%20sort_cited:y](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria%20sort_cited:y)
Sort by date of publication, the most recently published article being the first result given:
[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria%20sort_date:y](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria%20sort_date:y)

## Result Types

There are three options for the result type parameter which determine the fields returned, as follows:

- idlist : returns a list of IDs and sources for the given search terms

- lite : returns key metadata for the given search terms (default result type)

- core : returns full metadata for a given publication ID; including abstract, full text links, and MeSH terms

## Request Methods

## Format

The format can either be XML , JSON or DC (Dublin Core); the default value is XML if the parameter is unspecified. XML returns the same response as the SOAP web service; see the Web Service Reference Guide .

DC returns the following Dublin Core metadata fields, within an RDF/XML wrapper: dc:contributor , dc:creator , dc:date , dc:description , dc:identifier , dc:language, dc:subject , dc:title , dc:type , dcterms:abstract , dcterms:accessRights , dcterms:bibliographicCitation , dcterms:isPartOf , dcterms:isVersionOf .

The use of these fields complies with the DCMI Metadata Terms recommendation documentation. Additionally, it should be noted that dc:contributor fields are used for the organisations to which some, or all of the authors listed in the dc:creator fields are affiliated. dc:description contains the publication types of the record (e.g. "Journal Article", "Book", etc.) dcterms:accessRights is only included for works in the Open Access subset of the PMC collection. There are two dcterms:bibliographicCitation fields for each journal article record, one which matches the "Text (citation)" option in the export feature on the Europe PMC web site, the other a machine-readable format using the syntax of the OpenURL standard. Other publication types (e.g. books, patents) only contain a single, non-machine-readable dcterms:bibliographicCitation .

Publication dates have been mapped as follows: dc:date - first publication date (the date of first publication, whichever is first, electronic or print publication; where a date is not fully available e.g. year only, an algorithm is applied to determine the value), dc:terms:available - electronic publication date, dc:terms:created - print publication date.

Note that the ‘resulttype’ parameter associated with the DC response is always set to ‘core’.

Example:
[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=xml](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=xml)

[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=json](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=json)

[https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=dc](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=malaria&format=dc)

## Privacy Notice

We advise that you read our Privacy Notice before using this API. By using our public API you agree to accept the terms of the [Privacy Notice](https://www.ebi.ac.uk/data-protection/privacy-notice/embl-ebi-public-website/) .

Follow us

[News blog](http://blog.europepmc.org/)
Technical blog
[Bluesky](https://bsky.app/profile/europepmc.org)
YouTube

## Partnerships & funding

Europe PMC is developed by [EMBL-EBI](https://www.ebi.ac.uk/) with support from the [Europe PMC Funders' Group](https://europepmc.org/Funders/) , in collaboration with the [National Library of Medicine (NLM)](https://www.nlm.nih.gov/) , as part of the [PubMed Central International](https://www.ncbi.nlm.nih.gov/pmc/about/pmci/) archive network.

Europe PMC is an [ELIXIR Core Data Resource](https://elixir-europe.org/platforms/data/core-data-resources) , [Global Core Biodata Resource](https://globalbiodata.org/what-we-do/global-core-biodata-resources/) , and conforms with [EMBL-EBI’s long term data preservation policies](https://www.ebi.ac.uk/long-term-data-preservation) .
