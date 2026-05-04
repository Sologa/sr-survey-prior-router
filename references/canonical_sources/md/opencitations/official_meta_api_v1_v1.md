# opencitations (official_meta_api_v1)

Source URL: https://api.opencitations.net/meta/v1
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/opencitations/official_meta_api_v1_v1.html`

The REST API for OpenCitations Meta

#### The REST API for OpenCitations Meta

- DESCRIPTION

- PARAMETERS

- OPERATIONS

- /metadata/{ids}

- /author/{id}

- /editor/{id}

- HOME

# The REST API for OpenCitations Meta

Version: Version 1.1.1 (2022-12-22)

API URL: [https://api.opencitations.net/meta/v1](https://api.opencitations.net/meta/v1)

Contact: contact@opencitations.net

License: This document is licensed with a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode) , while the REST API itself has been created using [RAMOSE](https://github.com/opencitations/ramose) , the Restful API Manager Over SPARQL Endpoints created by [Silvio Peroni](https://orcid.org/0000-0003-0530-4305) , which is licensed with an [ISC license](https://opensource.org/licenses/ISC) .

## Description back to top

This is the REST API for OpenCitations Meta, the OpenCitations dataset containing bibliographic metadata associated with the documents involved in the citations stored in the OpenCitations Indexes. All the present operations return either a JSON document (default) or a CSV document according to the mimetype specified in the Accept header of the request. If you would like to suggest an additional operation to be included in this API, please use the [issue tracker](https://github.com/opencitations/api/issues) of the OpenCitations APIs available on GitHub.

API calls are rate-limited to 180 requests/minute per IP address to ensure fair usage and service availability. For large-scale data retrieval, please use the database dumps available at [download.opencitations.net](https://download.opencitations.net/) .

If you are going to use the REST APIs within an application/code, we encourage you to get the [OpenCitations Access Token](https://opencitations.net/accesstoken) and specify it in the "authorization" header of your REST API call. Here is a usage example in Python:
from requests import get API_CALL = "https://api.opencitations.net/meta/v1/metadata/doi:10.1007/978-1-4020-9632-7" HTTP_HEADERS = {"authorization": "YOUR-OPENCITATIONS-ACCESS-TOKEN"} get(API_CALL, headers=HTTP_HEADERS)

## Parameters back to top

Parameters can be used to filter and control the results returned by the API. They are passed as normal HTTP parameters in the URL of the call. They are:

-
require=<field_name> : all the rows that have an empty value in the <field_name> specified are removed from the result set - e.g. require=given_name removes all the rows that do not have any string specified in the given_name field.

-
filter=<field_name>:<operator><value> : only the rows compliant with <value> are kept in the result set. The parameter <operation> is not mandatory. If <operation> is not specified, <value> is interpreted as a regular expression, otherwise it is compared by means of the specified operation. Possible operators are "=", "<", and ">". For instance, filter=title:semantics? returns all the rows that contain the string "semantic" or "semantics" in the field title , while filter=date:>2016-05 returns all the rows that have a date greater than May 2016.

-
sort=<order>(<field_name>) : sort in ascending ( <order> set to "asc") or descending ( <order> set to "desc") order the rows in the result set according to the values in <field_name> . For instance, sort=desc(date) sorts all the rows according to the value specified in the field date in descending order.

-
format=<format_type> : the final table is returned in the format specified in <format_type> that can be either "csv" or "json" - e.g. format=csv returns the final table in CSV format. This parameter has higher priority of the type specified through the "Accept" header of the request. Thus, if the header of a request to the API specifies Accept: text/csv and the URL of such request includes format=json , the final table is returned in JSON.

-
json=<operation_type>("<separator>",<field>,<new_field_1>,<new_field_2>,...) : in case a JSON format is requested in return, tranform each row of the final JSON table according to the rule specified. If <operation_type> is set to "array", the string value associated to the field name <field> is converted into an array by splitting the various textual parts by means of <separator> . For instance, considering the JSON table [ { "names": "Doe, John; Doe, Jane" }, ... ] , the execution of array("; ",names) returns [ { "names": [ "Doe, John", "Doe, Jane" ], ... ] . Instead, if <operation_type> is set to "dict", the string value associated to the field name <field> is converted into a dictionary by splitting the various textual parts by means of <separator> and by associating the new fields <new_field_1> , <new_field_2> , etc., to these new parts. For instance, considering the JSON table [ { "name": "Doe, John" }, ... ] , the execution of dict(", ",name,fname,gname) returns [ { "name": { "fname": "Doe", "gname": "John" }, ... ] .

It is possible to specify one or more filtering operation of the same kind (e.g. require=given_name&require=family_name ). In addition, these filtering operations are applied in the order presented above - first all the require operation, then all the filter operations followed by all the sort operation, and finally the format and the json operation (if applicable). It is worth mentioning that each of the aforementioned rules is applied in order, and it works on the structure returned after the execution of the previous rule.

Example: <api_operation_url>?require=doi&filter=date:>2015&sort=desc(date) .

## Operations back to top

The operations that this API implements are:

- /metadata/{ids} : This operation retrieves the bibliographic metadata for each of the bibliographic entities identified by one or more input IDs

- /author/{id} : This operation retrieves the bibliographic metadata for each bibliographic entity authored by the person identified by the given ORCID or OpenCitations Meta Identifier.

- /editor/{id} : This operation retrieves the bibliographic metadata for each bibliographic entity edited by the person identified by the given ORCID or OpenCitations Meta Identifier.

### /metadata/{ids} back to operations

This operation retrieves the bibliographic metadata for each of the bibliographic entities identified by one or more input IDs

Each ID is built as follows: ID abbreviation + ":" = ID value. For example, For example "doi:10.3233/ds-170012" indicates a DOI identifier with value "10.3233/ds-170012"

The ID abbreviations currently supported in this operation are "doi", "issn", "isbn", and "omid"

It is possible to specify one or more IDs as input of this operation. In this case, the IDs should be separated with a double underscore ("__") – e.g. "doi:10.1108/jd-12-2013-0166__doi:10.1016/j.websem.2012.08.001". The fields returned by this operation are:

- id : the IDs of the bibliographic entity

- title : the title of the bibliographic entity

- author : the semicolon-separated list of authors of the bibliographic entity

- pub_date : the date of publication of the bibliographic entity

- venue : the title of the venue where the bibliographic entity has been published, followed by the list of identifiers referring that venue

- volume : the number of the volume in which the bibliographic entity has been published

- issue : the number of the issue in which the bibliographic entity has been published

- page : the starting and ending pages of the bibliographic entity in the context of the venue where it has been published

- type : the type of the bibliographic entity

Accepted HTTP method(s) get

Parameter(s) ids : type str , regular expression shape (doi|issn|isbn|omid|openalex|pmid|pmcid):.+?(__(doi|issn|isbn|omid|openalex|pmid|pmcid):.+?)*$

Result fields type id (str) , title (str) , author (str) , pub_date (datetime) , issue (str) , volume (str) , venue (str) , page (str) , type (str) , publisher (str) , editor (str)

Example [/metadata/doi:10.1007/978-1-4020-9632-7](https://api.opencitations.net/meta/v1/metadata/doi:10.1007/978-1-4020-9632-7)

Exemplar output (in JSON)
[ { "id": "doi:10.1007/978-1-4020-9632-7 isbn:9781402096327 isbn:9789048127108 openalex:W4249829199 omid:br/0612058700", "title": "Adaptive Environmental Management", "author": "", "pub_date": "2009", "page": "", "issue": "", "volume": "", "venue": "", "type": "book", "publisher": "Springer Science And Business Media Llc [crossref:297 omid:ra/0610116006]", "editor": "Allan, Catherine [orcid:0000-0003-2098-4759 omid:ra/069012996]; Stankey, George H. [omid:ra/061808486861]" } ]

### /author/{id} back to operations

This operation retrieves the bibliographic metadata for each bibliographic entity authored by the person identified by the given ORCID or OpenCitations Meta Identifier.

Both ORCID and OMID must be specified preceded by a prefix that makes explicit the identifier scheme, i.e. orcid: for ORCID (e.g., orcid:0000-0003-1572-6747 ) and omid: for OMID (e.g., omid:ra/0601 ).

The fields returned by this operation are:

- id : the IDs of the bibliographic entity

- title : the title of the bibliographic entity

- author : the semicolon-separated list of authors of the bibliographic entity

- pub_date : the date of publication of the bibliographic entity

- venue : the title of the venue where the bibliographic entity has been published, followed by the list of identifiers referring that venue

- volume : the number of the volume in which the bibliographic entity has been published

- issue : the number of the issue in which the bibliographic entity has been published

- page : the starting and ending pages of the bibliographic entity in the context of the venue where it has been published

- type : the type of the bibliographic entity

Accepted HTTP method(s) get

Parameter(s) id : type str , regular expression shape ((orcid:)?([0-9]{4}-){3}[0-9]{3}[0-9X])|(omid:ra\/06[1-9]*0\d+)

Result fields type id (str) , title (str) , author (str) , pub_date (datetime) , issue (str) , volume (str) , venue (str) , page (str) , type (str) , publisher (str) , editor (str)

Example [/author/orcid:0000-0002-8420-0696](https://api.opencitations.net/meta/v1/author/orcid:0000-0002-8420-0696)

Exemplar output (in JSON)
[ { "id": "doi:10.1007/s11192-022-04367-w openalex:W3214893238 omid:br/061202127149", "title": "Identifying And Correcting Invalid Citations Due To DOI Errors In Crossref Data", "author": "Cioffi, Alessia [orcid:0000-0002-9812-4065 omid:ra/061206532419]; Coppini, Sara [orcid:0000-0002-6279-3830 omid:ra/061206532420]; Massari, Arcangelo [orcid:0000-0002-8420-0696 omid:ra/06250110138]; Moretti, Arianna [orcid:0000-0001-5486-7070 omid:ra/061206532421]; Peroni, Silvio [orcid:0000-0003-0530-4305 omid:ra/0614010840729]; Santini, Cristian [orcid:0000-0001-7363-6737 omid:ra/067099715]; Shahidzadeh, Nooshin [orcid:0000-0003-4114-074X omid:ra/06220110984]", "pub_date": "2022-06", "issue": "6", "volume": "127", "venue": "Scientometrics [issn:0138-9130 issn:1588-2861 openalex:S148561398 omid:br/0626055628]", "type": "journal article", "page": "3593-3612", "publisher": "Springer Science And Business Media Llc [crossref:297 omid:ra/0610116006]", "editor": "" }, { "id": "doi:10.5334/johd.178 omid:br/06404693975", "title": "The Integration Of The Japan Link Center\u2019s Bibliographic Data Into OpenCitations", "author": "Heibi, Ivan [orcid:0000-0001-5366-5194 omid:ra/064013186642]; Massari, Arcangelo [orcid:0000-0002-8420-0696 omid:ra/064013186643]; Moretti, Arianna [orcid:0000-0001-5486-7070 omid:ra/061206532421]; Peroni, Silvio [orcid:0000-0003-0530-4305 omid:ra/064013186644]; Rizzetto, Elia [orcid:0009-0003-7161-9310 omid:ra/064013186645]; Soricetti, Marta [orcid:0009-0008-1466-7742 omid:ra/064013186641]", "pub_date": "2024", "issue": "", "volume": "10", "venue": "Journal Of Open Humanities Data [issn:2059-481X openalex:S4210240912 omid:br/06160186133]", "type": "journal article", "page": "", "publisher": "Ubiquity Press, Ltd. [crossref:3285 omid:ra/0610116010]", "editor": "" }, { "id": "doi:10.1007/978-3-031-16802-4_36 openalex:W4295990858 omid:br/061603442625", "title": "Enabling Portability And Reusability Of Open Science Infrastructures", "author": "Grieco, Giuseppe [orcid:0000-0001-5439-4576 omid:ra/061609362356]; Heibi, Ivan [orcid:0000-0001-5366-5194 omid:ra/063011864088]; Massari, Arcangelo [orcid:0000-0002-8420-0696 omid:ra/06250110138]; Moretti, Arianna [orcid:0000-0001-5486-7070 omid:ra/061206532421]; Peroni, Silvio [orcid:0000-0003-0530-4305 omid:ra/0614010840729]", "pub_date": "2022", "issue": "", "volume": "", "venue": "Linking Theory And Practice Of Digital Libraries [isbn:9783031168017 isbn:9783031168024 omid:br/061603442934]", "type": "book chapter", "page": "379-385", "publisher": "Springer Science And Business Media Llc [crossref:297 omid:ra/0610116006]", "editor": "" } ]

### /editor/{id} back to operations

This operation retrieves the bibliographic metadata for each bibliographic entity edited by the person identified by the given ORCID or OpenCitations Meta Identifier.

Both ORCID and OMID must be specified preceded by a prefix that makes explicit the identifier scheme, i.e. orcid: for ORCID (e.g., orcid:0000-0003-1572-6747 ) and omid: for OMID (e.g., omid:ra/0601 ).

The fields returned by this operation are:

- id : the IDs of the bibliographic entity

- title : the title of the bibliographic entity

- author : the semicolon-separated list of authors of the bibliographic entity

- pub_date : the date of publication of the bibliographic entity

- venue : the title of the venue where the bibliographic entity has been published, followed by the list of identifiers referring that venue

- volume : the number of the volume in which the bibliographic entity has been published

- issue : the number of the issue in which the bibliographic entity has been published

- page : the starting and ending pages of the bibliographic entity in the context of the venue where it has been published

- type : the type of the bibliographic entity

Accepted HTTP method(s) get

Parameter(s) id : type str , regular expression shape ((orcid:)?([0-9]{4}-){3}[0-9]{3}[0-9X])|(omid:ra\/06[1-9]*0\d+)

Result fields type id (str) , title (str) , author (str) , pub_date (datetime) , issue (str) , volume (str) , venue (str) , page (str) , type (str) , publisher (str) , editor (str)

Example [/editor/orcid:0000-0003-2098-4759](https://api.opencitations.net/meta/v1/editor/orcid:0000-0003-2098-4759)

Exemplar output (in JSON)
[ { "id": "doi:10.1007/978-1-4020-9632-7 isbn:9781402096327 isbn:9789048127108 openalex:W4249829199 omid:br/0612058700", "title": "Adaptive Environmental Management", "author": "", "pub_date": "2009", "issue": "", "volume": "", "venue": "", "type": "book", "page": "", "publisher": "Springer Science And Business Media Llc [crossref:297 omid:ra/0610116006]", "editor": "Allan, Catherine [orcid:0000-0003-2098-4759 omid:ra/069012996]; Stankey, George H. [omid:ra/061808486861]" } ]

This API and the related documentation has been created with [RAMOSE](https://github.com/opencitations/ramose) , the Restful API Manager Over SPARQL Endpoints , developed by [Silvio Peroni](http://orcid.org/0000-0003-0530-4305) and [Marilena Daquino](https://marilenadaquino.github.io) .
