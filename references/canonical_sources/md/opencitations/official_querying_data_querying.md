# opencitations (official_querying_data)

Source URL: https://opencitations.net/querying/
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/opencitations/official_querying_data_querying.html`

Querying Data - OpenCitations

Close Search
Search for: Search

Skip to content

[OpenCitations](https://opencitations.net/)

Menu

- [Home Page](https://opencitations.net/)

- About

- [Story](https://opencitations.net/our-story/)

- [Team](https://opencitations.net/our-team/)

- [Governance](https://opencitations.net/governance/)

- [Why OpenCitations?](https://opencitations.net/why-opencitations/)

- [Mission](https://opencitations.net/mission/)

- [What we do](https://opencitations.net/what-we-do/)

- Support us

- [How to](https://opencitations.net/support-opencitations/)

- [Members & Donors](https://opencitations.net/members-and-donors/)

- [FAQs](https://opencitations.net/faqs/)

- Community

- [Partner Projects](https://opencitations.net/partner-projects/)

- [Awards](https://opencitations.net/awards/)

- [Publications](https://opencitations.net/publications/)

- News

- [Blog](https://opencitations.hypotheses.org/)

- [Newsletter](https://opencitations.net/newsletter/)

- More

Search for: Search

Open Search

# Querying Data

## Querying Data

OpenCitations provides three main mechanisms to query the data it provides.

### SPARQL endpoints

Open Citations made available a [SPARQL](https://www.w3.org/TR/sparql11-query/) endpoint for all the datasets released. When such a SPARQL endpoint is accessed with a browser, it shows an editor GUI generated with [YASGUI](https://yasgui.org/) . Of course, any SPARQL endpoint can additionally be queried using the [SPARQL Protocol](https://www.w3.org/TR/sparql11-protocol/) , e.g. via curl . The SPARQL endpoints available are:

- [Open](https://sparql.opencitations.net/index) [Citations](https://sparql.opencitations.net/index) [Index SPARQL endpoint](https://sparql.opencitations.net/index)

- [Open](https://sparql.opencitations.net/meta) [Citations](https://sparql.opencitations.net/meta) [Meta SPARQL endpoint](https://sparql.opencitations.net/meta)

### REST APIs

All the data in any of the Open Citations datasets can be retrieved by using an HTTP REST API. The rationale of making REST APIs available in addition to the SPARQL endpoints was to provide convenient access to the data included in the Open Citations datasets for Web developers and users who are not necessarily experts in Semantic Web technologies. All the REST APIs made available by Open Citations , has been implemented by means of [RAMOSE, the Restful API Manager Over SPARQL Endpoints](https://github.com/opencitations/ramose) , which is a Python application that allows one to simply create a REST API over any SPARQL endpoint by means of a simple configuration file that execute a SPARQL query dependently of the particular API call specified. The REST APIs available are:

- [Open](https://api.opencitations.net/index/v2) [Citations](https://api.opencitations.net/index/v2) [Index REST API](https://api.opencitations.net/index/v2)

- [Open](https://api.opencitations.net/meta/v1) [Citations](https://api.opencitations.net/meta/v1) [Meta REST API](https://api.opencitations.net/meta/v1)

If you are going to use the REST APIs within an application/code, we encourage you to first get the OpenCitations Access Token and specify it in the “authorization” header of your REST API call. Obtaining the token takes only a few seconds and needs to happen only once. It costs you nothing, however, it could help Open Citations a lot. Thank you!

### Search Interfaces

Open Citations has additionally developed user-friendly text search interfaces and browsing interfaces that can be used to search data in all the Open Citations datasets and to visualise and browse them, respectively. These two interfaces have been developed by means of [OSCAR, the](https://github.com/opencitations/oscar) [Open](https://github.com/opencitations/oscar) [Citations](https://github.com/opencitations/oscar) [RDF Search Application](https://github.com/opencitations/oscar) , and [LUCINDA, the](https://github.com/opencitations/lucinda) [Open](https://github.com/opencitations/lucinda) [Citations](https://github.com/opencitations/lucinda) [RDF Resource Browser](https://github.com/opencitations/lucinda) , that provide a configurable layer over SPARQL endpoints that permit one easily to create Web interfaces for querying and visualising the results of SPARQL queries. The search interfaces available are:

- [Open](https://search.opencitations.net/) [Citations](https://search.opencitations.net/) [Search Interface](https://search.opencitations.net/)

###### OPENCITATIONS

OpenCitations is managed by the [Research Centre for Open Scholarly Metadata](https://openscholarlymetadata.org/) , an independent research centre within the [University of Bologna](https://www.unibo.it/en) .

###### LICENSE

The data held in any of the OpenCitations datasets are available under a [Creative Commons public domain dedication (CC0)](https://creativecommons.org/public-domain/cc0/) . The text of the web pages that comprise the OpenCitations website is available under a [Creative Commons Attribution 4.0 International Public License.](https://creativecommons.org/licenses/by/4.0/deed.en) The software is available on [GitHub](https://github.com/opencitations) under the [ISC License.](https://opensource.org/licenses/ISC)

###### PRIVACY POLICY

## The use of the OpenCitations trademark is subject to the OpenCitations TRADEMARK POLICY AND BRAND GUIDELINES

###### CONTACTS

For general inquiries, please contact:
contact@opencitations.net

For assistance with OpenCitations services, please contact:
tech@opencitations.net

[Your opinion matters](https://opencitations.net/feedback-page/)

[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | OpenCitations

- Mail

- [GitHub](http://github.com/opencitations)

- [X](https://x.com/opencitations)

- [LinkedIn](https://www.linkedin.com/company/opencitations/)

- [Mastodon](https://scicomm.xyz/@opencitations)

- [Bluesky](https://bsky.app/profile/opencitations.bsky.social)

OpenCitations
