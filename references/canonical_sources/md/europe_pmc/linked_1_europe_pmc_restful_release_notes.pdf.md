# Europe PMC REST and bulk services (linked_1)

Source URL: https://europepmc.org/docs/Europe_PMC_RESTful_Release_Notes.pdf
Local raw file: `references/canonical_sources/raw/europe_pmc/linked_1_europe_pmc_restful_release_notes.pdf.pdf`



## Page 1

Europe PMC RESTful Web Service release history
----------------- 2023-08-31 -----------------
* Europe PMC RESTful Web Service
V6.9.0
Release Git tag: epmc-rest-6.9.0
Release date 2023-08-16 to the test environment
2023-08-31 to production system
Items addressed:
CIT-8365
Added a new rest API endpoint to search peer
reviews/evaluations available for an article.
CIT-8364
Included hasEvaluations field in the top level core response of
the article as well as corresponding to its versions.
Fields Added:
"hasEvaluations" - in the outer core response of the article.
"hasEvaluations" - in the version element, inside the
versionList field of the core response.
New search field:
HAS_VERSION_EVALUATIONS:(Y/N)
----------------- 2022-05-11 -----------------
* Europe PMC RESTful Web Service
V6.8.0
Release Git tag: epmc-rest-6.8.0
Release date 2022-04-28 to the test environment
2022-05-11 to production system
Items addressed:
CIT-7405
Add new API endpoint for article ID
CIT-2336
SOAP: bug or feature,If we don't put a queryString the
TextQueryResolver is using the default "*:*"
CIT-7864
Adjusting Logs Rolling strategy for both SOAP and REST
----------------- 2021-11-29 -----------------
* Europe PMC RESTful Web Service
V6.7.0
Release Git tag: epmc-rest-6.7.0
Release date
2021-11-29 to the test environment
2021-11-29 to production system
Items addressed:
CIT-7401
Modify web services to enable user to submit a batch of article
IDs and retrieve a status update



## Page 2

----------------- 2021-08-03 -----------------
* Europe PMC RESTful Web Service
V6.6.0
Release Git tag: epmc-rest-6.6.0
Release date
2021-08-17 to the test environment
2021-08-31 to production system
Items addressed:
CIT-7376
Add "pubTypeList" to "version" element to select from CDB
CIT-7392
Add "pubTypeList" to "version" element in mongo and WS
CIT-7066
Improvement to Rest APIs design - add nextPageUrl and provide
support for Accept header
----------------- 2020-10-26 -----------------
* Europe PMC RESTful Web Service
V6.5.0
Release Git tag: epmc-rest-6.5.0
Release date
2020-10-12 to the test environment
2020-10-26 to production system
Items addressed:
CIT-6560
Added affiliationOrgId for each author affiliation, inside the
<authorAffiliationDetailsList> section, in the web service response
CIT-6561
Move the organization id field from the main author level to the
single affiliation level inside mongoDB document
----------------- 2020-07-14 -----------------
* Europe PMC RESTful Web Service
V6.4.0
Release Git tag: epmc-rest-6.4.0
Release date
2020-07-01 to the test environment
2020-07-14 to production system
Items addressed:
CIT-6559
Added 'fullTextId' in core response, inside the fullTextIdList field
CIT-6484
Remove full text licence statement in search index
----------------- 2020-05-27 -----------------
* Europe PMC RESTful Web Service
V6.3.0
Release Git tag: epmc-rest-6.3.0
Release date
2020-05-12 to the test environment



## Page 3

2020-05-28 to production system
Items addressed:
CIT-3255
Included datalinks tags to the webservices core response
CIT-6388
Added publication status field to the web service core response
CIT-6471
Removed the textMinedTerms method from REST/SOAP api
----------------- 2019-04-25 -----------------
* Europe PMC RESTful Web Service
V6.2.0
Release Git tag: epmc-rest-6.2.0
Release date
2018-10-07 to the test environment
2018-10-21 to production system
Items addressed:
CIT-5425
Add fulltext received date for web services response
CIT-5084
index date received for fulltext content
CIT-5423
Add org_id in solr and web services response
----------------- 2019-04-25 -----------------
* Europe PMC RESTful Web Service
V6.1.0
Release Git tag: epmc-rest-6.1.0
Release date
2018-04-11 to the test environment
2018-04-25 to production system
Items addressed:
CIT-4984
Added new index fields ANNOTATION_TYPE and ANNOTATION_PROVIDER
CIT-4609
Added new index field FIRST_IDATE. Added fields firstIndexDate and
versionNumber to both lite and core response. Added field
versionList to the core response.
----------------- 2018-03-28 -----------------
* Europe PMC RESTful Web Service
V6.0.0
Release Git tag: epmc-rest-6.0.0
Release date
2018-03-28 to the test environment
2018-04-19 to production system
Items addressed:
CIT-2498 Add Swagger documentation.



## Page 4

----------------- 2018-01-16 -----------------
* Europe PMC RESTful Web Service
v5.3.2
Release Git tag: rel_20180116_532_datalinks
Release date
2018-01-16 to the test environment
2018-01-23 to production system
Items addressed:
CIT-2525 Add link counts for sections and categories.
----------------- 2017-12-13 -----------------
* Europe PMC RESTful Web Service
v5.3.0
Release Git tag: rel_20171211_530_datalinks
Release date
2017-12-13 to the test environment
2018-01-10 to production system
Items addressed:
CIT-2520 The datalinks webservice method was added to consolidate the output
of the labslinks,databaseLinks and textMinedTerms API methods.
CIT-2524 Design of new API module.
CIT-2525 Implement the new API module.
CIT-3113 Add parameter to limit the number of results and sort results by
frequency
CIT-3255 Add datalinks tags to webservices core response
----------------- 2017-05-10 -----------------
* Europe PMC RESTful Web Service
v5.2.0
Release Git tag: rel_20170425_029_520_suppl
Release date
2017-04-25 to the test environment
2017-05-10 to production system
Items addressed:
CIT-2715
The response element "firstPublicationDate" of the
searchPublications webmethod is now part of the "lite" response
as well.
CIT-1796
Adding a new request parameter "inlineImages" to the
"getSupplementaryFiles" request.
CIT-2341
Added a POST method "searchPOST" to the RESTful web service. Has
the same parameters as the “search” web method.
CIT-2958
Request parameter "synonym" changed from type Boolean to String and
is accepting the following parameter: "True", "Y", "YES", "FALSE",
"N" or "NO" (case insensitive).
CIT-2969
RESTful: in the "search" request the property "resultType" is now
also available in camelCase.
----------------- 2017-03-08 -----------------
* Europe PMC RESTful Web Service



## Page 5

v5.1.0
Release Git tag: rel_20170308_027_510_authManAndPrideAndDoiHttps
Release date
2017-03-08 to the test environment
2017-03-29 to production system
Items addressed:
CIT-2728
Adding PRIDE references
CIT-2672
Adding authMan, nihAuthMan and manuscriptId field to web service
core response. Also moving epmcAuthMan from lite to the core
response.
----------------- 2017-03-07 -----------------
* Europe PMC RESTful Web Service
v5.0.1
Release Git tag: rel_20170307_026_501_doiAndBackwardsCompatibility
Release date
n/a
to the test environment
2017-03-07 to production system
Items addressed:
CIT-2338
DOI URL format change



## Page 6

----------------- 2017-02-09 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20170209_024_mongo (v5.0)
Release date
n/a
to the test environment
2017-02-09 to production system
Items addressed:
CIT-2577
Mongo DB Data fetching for core response
CIT-2716
Added bookOrReportDetails to the lite response
CIT-2701
Fixed synonyms parameter
----------------- 2017-02-02 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20170202_023_Preprints_PRIDE (v4.5.4)
Release date
n/a
to the test environment
2017-02-02 to production system
Items addressed:
CIT-2295
Adding PRIDE XREFS as a new Bio Entity to the "databaseLinks"
request.
E.g. .../rest/MED/11805837/databaseLinks/PRIDE
Read more about the PRIDE archive here.
----------------- 2016-10-13 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20161013_016_cursorMarkAndSort (v4.5.3)
Release date
2016-10-06 to the test environment
2016-10-13 to production system
Items addressed:
CIT-2221
Replacement of the request parameter "offset" with "cursorMark"
for the SOAP method "searchPublications" and the RESTful method
"search".
E.g. .../rest/search/query=(p55)...&sort=CITED%20asc&cursorMark=*
Read more about in the Apache Wiki: Pagination of Results
CIT-2329
New example for pagination through a result list in the PERL
client.
CIT-2275
Added a new "sort" request for the SOAP method
"searchPublications" and the RESTful method "search". This field
provides "asc" or "desc" order for every single-valued field,
e.g. P_PDATE, AUTH_FIRST, CITED etc.
CIT-2327
The "epmcAuthMan" response element will now be returned
correctly.
Minor items addressed: CIT-2275, CIT-2274, CIT-2320, CIT_2301, CIT-2318,
CIT_2319, CIT-2303, CIT-2329, CIT-2340, CIT-2292, CIT-2306.
----------------- 2016-07-01 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20160701_015_labsLinkImg (v4.5.2)
Release date
2016-07-05 to the test environment
2016-07-12 to production system
Items addressed:
CIT-2125
Added new element "imgUrl" in the "labsLinks" section.
More detailed: Adding support for external links providers to
provide images with their links. The image URLs are stored in the
database and are exposed through the WSs to the front-end.



## Page 7

E.g. .../rest/med/8206158/labsLinks/1562/
CIT-2116
Returning the "pubYear" in both result types: CORE and LITE.
Before the "pubYear" was only returned in the LITE response.
----------------- 2016-05-12 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20160512_014_embargoedMan (v4.5.1)
Release date
2016-05-12 to the test environment
2016-05-19 to production system
Items addressed:
CIT-1541
Fixed the sorting of the results of the getCitations method.
CIT-2093
Fixed a bug regarding to the usage of wildcards in the range
queries. E.g. EMBARGO_DATE:[20160101 TO *].
CIT-1820
Added new boolean field named EMBARGOED_MAN, values are Y or N.
This field will be translated into an EMBARGO_DATE range query.
Assuming you request EMBARGOED_MAN:Y at the date 20160101 than
this will be translated into EMBARGO_DATE:[20160101 TO *] and
EMBARGOED_MAN:N to EMBARGO_DATE:[* TO 20160101].



## Page 8

----------------- 2016-01-21 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20160121_012_hasSuppl (v4.5.0)
Release date: 2016-01-21
Items addressed:
CIT-1868:
Appended HAS_SUPPL to the WS response, indicates the existence of
supplemental data e.g. spreadsheets, video files, etc.
----------------- 2015-11-18 -----------------
* Europe PMC RESTful Web Service
Release Git tag: rel_20151118_010_hasPDF (v4.4)
Release date: 2015-11-18
Items addressed:
CIT-1672:
Added the hasPDF element to the ‘lite’ and ‘core’ responses of
the search module. This indicates whether a publisher has
provided a PDF version of an article.
Performance improvements made.
----------------- 2015-05-20 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_2015-05-20_2step-orcid (v4.1)
Release date: 2015-05-20
Items addressed:
CIT-1087:
Web service modified to allow an ORCID search to be made without
the need to specify the ‘AURTHORID’ search term, for example:
http://www.ebi.ac.uk/europepmc/webservices/rest/search/query=0000
-0002-3900-643X
----------------- 2015-02-25 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rel_2015-02-25_dates (v4.1)
Release date: 2015-02-25
Items addressed:
CIT-1235:
Web service modified to include new dates in XML and Dublin Core
responses. XML/DC elements:
electronicPublicationDate/dc:terms:available,
firstPublicationDate/dc:date,
printPublicationDate/dc:terms:created,
embargoDate (XML only).
----------------- 2014-12-10 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_4_0
Release date: 2014-12-10
Items addressed:
1.
Removed the dataset parameter from the ‘profile’ and ‘search’
modules.
2.
Changed the default value of the synonym parameter to ‘false’ for



## Page 9

the ‘profile’ and ‘search’ modules.
----------------- 2014-07-21 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_1_6
Release date: 2014-07-21
Tickets addressed:
CIT-1031:
Add Synonym Option to both Search Publications and Profile
Publications methods. This option has two values either TRUE or
FALSE
CIT-625:
This version has an ability to search for licenses with the new
index field called LICENSE. Examples: LICENSE:cc ; LICENSE:cc-by
----------------- 2014-07-09 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: affiliations-efo_20140701
Release date: 2014-07-09
Tickets addressed:
CIT-1012:
Multiple author affiliations per article.
CIT-1201:
Web service extension for EFO – see textMinedTerms module
documentation.



## Page 10

----------------- 2014-07-10 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: missing-keywords_20140710
Release date: 2014-07-10
Tickets addressed:
CIT-1242:
Missing keywords in web service.
----------------- 2014-04-15 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: dc_release
Release date: 2014-04-15
Tickets addressed:
CIT-1085:
Added new Dublin Core response
Other:
●
Changed PUB_TYPE delimiter comma to semicolon (;)
●
Removed query length restriction.
●
Fixed bug in the ID search methods: 2 digit external id
searches not working
●
Redirect index.html to official help page
●
Handle correctly ‘callback’ parameter (TRK:24041336)
----------------- 2014-06-04 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_1_5
Release date: 2014-06-04
Tickets addressed:
CIT-1016:
Added first names into the ‘core’ response of the ‘search’
module.
CIT-1196:
Vernacular title used when the actual title is blank.
----------------- 2013-07-11 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_1_2
Release date: 2013-07-11
Tickets addressed:
CIT-833:
New ‘labsLinks’ module created for the new Europe PMC External
Links Service. Europe PMC RESTful (articles) page updated with
the module details and examples.
New search fields:
HAS_LABSLINKS:Y
AUTHORID_TYPE:ORCID
AUTHORID:0000-0002-9958-7213
----------------- 2013-11-18 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_1_3
Release date: 2013-11-18
Tickets addressed:
CIT-974:
ORCID information added into the response of the ‘search’
module.
----------------- 2013-05-20 -----------------
* Europe PMC RESTful Web Service



## Page 11

Release CVS tag: rest_release_1_1
Release date: 2013-05-20
Tickets addressed:
CIT-867:
'citationType' element does not display in RESTful 'citations'
module TRK:28031355
Details:
‘citationType’ element was showing null values in JSON response,
and no values for the XML response for citations module. The
JSON response has been corrected to agree with the XML response.
Feature request (CIT-868) logged to show ‘CitationType’ values
in the ‘citations’ module.
CIT-869:
RESTful Response: PUB_TYPE only shows one value TRK:02051254
Details:
The Index fields PUB_TYPE, ACCESSION_TYPE, with repeating
values, now presented with comma separated values. For ISSN,
when there are two values, the second value is placed in ESSN.
CIT-870:
RESTful Web Service: New Features Release (investigators/
accession numbers)
New Features:
a. New elements in CORE:
Added Investigators to the CORE response.
<investigatorList>
b. Added Array Express data to the databaseLinks module and also
added <dbName>ARXPR</dbName> to the <dbCrossReferenceList> of
the LITE response.
c. Text mined accessions information like ACCESSION_ID and
ACCESSION_TYPE in the dataset:metadata
d. New elements in LITE:
i.
<dbName>ARXPR</dbName> to the <dbCrossReferenceList>
ii.
<hasTMAccessionNumbers>
iii.
Added <tmAccessionTypeList>, if
<hasTMAccessionNumbers>is YES
New search fields:
●
INVESTIGATOR:"Ana Belén" (where Ana Belén are first names of
INVESTIGATOR:"Ana Belén Fernández")
●
HAS_ARXPR:y
●
ARXPR_PUBS:E-GEOD-22481
●
ACCESSION_ID:PF00072 (to metadata)
●
ACCESSION_TYPE:gen
----------------- 2013-03-14 -----------------
* Europe PMC RESTful Web Service
Release CVS tag: rest_release_1_0
Release date: 2013-03-14
Web Service first release.
