# dimensions_api (official_api_access)

Source URL: https://docs.dimensions.ai/dsl/api.html
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/dimensions_api/official_api_access_api.html.html`

API Access — DSL 2.14 documentation

DSL

- Getting Started Checklist

- A Tour of the DSL

- Query Syntax

- Functions Syntax

- Expert Identification

- Data Sources

- Example Queries and Results

- API Access

- Getting an API Key

- Querying the API

- API Endpoints

- Python : raw access

- Python : Dimcli

- curl + jq

- PowerShell

- Postman

- Third-party Libraries and Tools

- Google Sheets / Excel Add-in

- Glossary

- Reasonable Use

- Release Notes and Deprecations

- Frequently Asked Questions

DSL

-

- API Access

-

# API Access 

The Dimensions Analytics API is subscription-only, so your Dimensions account needs to be activated for this service and subject to restrictions on use.

## Getting an API Key 

Once you have API access, you’ll be able to generate a new API Key by going to the ‘My Account’ section of the Dimensions web application.

Note

For CRIS API homepage, API Key can be located at [https://cris-api.dimensions.ai/v3/home/](https://cris-api.dimensions.ai/v3/home/) . Follow instructions on this page regarding the API usage as well.

## Querying the API 

Querying the Dimensions API always involves two steps :

-
Sending your credentials (key) to the authentication url, in order to retrieve a query token .

-
Sending the token and a DSL query to the query url, in order to retrieve JSON data .

Important

The Dimensions Analytics API, and CRIS API is limited to 30 requests per IP address per minute. The query token is valid for around 2 hours so it should be reobtained when it expires.

The diagram below provides an overview of these operations.

### API Endpoints 

The API includes two groups of endpoints: a) for authentication and b) for querying.

The authentication endpoint is the same for all versions of the API. The querying endpoints instead are for specific versions of the API.

Authentication Endpoint 

Name

Endpoint Path

Description

API Authentication

/api/auth

The single authentication endpoint for all API versions. Returns a query token.

Querying Endpoints 

Name

Endpoint Path

Description

V1 (legacy)

/api/dsl/v1

V1 API. Currenlty in maintenance mode. Removed in March 2022.

V2 (latest)

/api/dsl/v2

V2 API. Current major version of the DSL.

Current (alias)

/api/dsl

Alias for current version of API. Will point to V1 till Dec 2021, then will point to V2.

Current (alias, alternative path)

/api/dsl.json

Alias for current version of API. Will point to V1 till Dec 2021, then will point to V2.

Important

Add your Dimensions URL to the endpoint path in order to obtain the final API URL. Eg if your Dimensions URL is https://app.dimensions.ai , your final authentication URL will be https://app.dimensions.ai/api/auth .

## Python : raw access 

The following code snippet shows how to connect to the Dimensions API only using Python’s requests library.

import requests # The credentials to be used login = { 'key' : "your API key" } # Send credentials to login url to retrieve token. Raise # an error, if the return code indicates a problem. # Please use the URL of the system you'd like to access the API # in the example below. resp = requests . post ( 'https://<your-url.dimensions.ai>/api/auth' , json = login ) resp . raise_for_status () # Create http header using the generated token. headers = { 'Authorization' : "JWT " + resp . json ()[ 'token' ] } # Execute DSL query. resp = requests . post ( 'https://<your-url.dimensions.ai>/api/dsl/v2' , data = 'search publications return publications' . encode (), headers = headers ) # Display raw result print ( resp . json ())

The snippet above uses the key authentication method, which is the primary method for most API servers (see also [this page](https://dimensions.freshdesk.com/support/solutions/articles/23000018791) for more information on how to obtain a key).

Note

Please note escaping rules in [Python](http://python-reference.readthedocs.io/en/latest/docs/str/escapes.html) . For example, when writing a query with escaped quotes, such as:

search publications for "\"phrase 1\" AND \"phrase 2\""

in Python, it is necessary to escape the backslashes as well, so it would look like:

resp = requests.post( 'https://<your-url.dimensions.ai>/api/dsl/v2', data='search publications for "\\"phrase 1\\" AND \\"phrase 2\\""', headers=headers)

Similar escaping rules might apply to other programming languages than Python as well. Alternatively , Using triple quotes can be used to avoid having to escape quote characters.

## Python : Dimcli 

Dimensions APIs can be accessed also using [Dimcli](https://digital-science.github.io/dimcli/getting-started.html) , an open-source Python client. Dimcli is a convenient way to connect to, query and analyze the results of Dimensions API.

import dimcli dimcli . login ( key = "123456789qwertyuiop" , endpoint = "https://app.dimensions.ai/api/dsl/v2" ) dsl = dimcli . Dsl () data = dsl . query ( """search grants for "malaria" return researchers""" ) print ( data . json ) # {'researchers': [{'id': 'ur.01332073522.49', # 'count': 75, # 'last_name': 'White', # 'first_name': 'Nicholas J'}, # {'id': 'ur.01343654360.43', # 'count': 59, # 'last_name': 'Marsh', # 'first_name': 'Kevin'}, # ............. # ], # '_stats': {'total_count': 8735}}

The API Lab includes several notebooks demonstrating the practical use of Dimcli. In particular, these two are a good place to start:

-
[The Dimcli Python library: Installation and Querying](https://api-lab.dimensions.ai/cookbooks/1-getting-started/1-Using-the-Dimcli-library-to-query-the-API.html)

-
[The Dimcli Python library: Working with Pandas Dataframes](https://api-lab.dimensions.ai/cookbooks/1-getting-started/3-Working-with-dataframes.html)

Note

Dimcli includes also a command line interface (CLI) that makes it easier to learn the grammar of the Dimensions Search Language. Calling dimcli from a Terminal opens an interactive query console with syntax autocompletion, persistent history across sessions, pretty-printing and preview of JSON results, export to HTML and CSV, and more.

## curl + jq 

This example shows a minimal way to query the API. This should be easily transferable to any other programming language or environment.

export DSL_TOKEN = $( curl https://<your-url.dimensions.ai>/api/auth.json -d '{"key": "your API key"}' -s | jq -r .token ) curl https://<your-url.dimensions.ai>/api/dsl/v2 -H "Authorization: JWT $DSL_TOKEN " -d 'search publications return publications' -s | jq

Note

Note that jq tool is used to extract a “token” value from the JSON response in the first request. In the second request, jq is used only to pretty print the result so it’s use is optional.

## PowerShell 

This is an equivalent example of the above CURL + JQ Example, but usable in the PowerShell enivornment.

$DSL_TOKEN = ( Invoke-RestMethod -Uri https://<your-url.dimensions.ai>/api/auth.json -Method Post -Body ( @ { 'key' = 'your API key' } | ConvertTo-JSON )) .token Invoke-RestMethod -Uri https://<your-url.dimensions.ai>/api/dsl/v2 -Method Post -H @ { Authorization = "JWT $DSL_TOKEN " } -Body 'search publications return publications'

## Postman 

This examples shows how to set up [Postman](https://www.getpostman.com) to query the Dimensions API. This can be achieved in two simple steps.

1. Obtaining a JWT token

Make a POST request to https://app.dimensions.ai/api/auth.json with body { "key": "<your-API-key>"}

This will return a JWT token, which should be noted as it will be used in the next step.

2. Using the token to query the API

Make a new POST request by adding the token to the Headers panel in this format: Authorization : JWT {theToken} .

Finally, Compose your query in the request body section:

Note

Another approach to get started with Postman is by using the [cURL importer](https://learning.getpostman.com/docs/postman/collections/data_formats/#importing-curl) .

## Third-party Libraries and Tools 

dimensionsR Library

The [dimensionsR library](https://github.com/massimoaria/dimensionsR) is an open-source R-package to gather bibliographic data using the Dimensions API and the DSL.

rdimensions Library

Another client library [rdimensions](https://github.com/nicholasmfraser/rdimensions) for interacting with the Dimensions API from the R environment.

Sidewall Python Library

The [Sidewall library](https://github.com/caltechlibrary/sidewall) is a Python package providing object classes for Dimensions entities, fetches data incrementally, caches results, copes with rate limits, and more, to make working with Dimensions in Python more natural.

Biblioshiny

Bibliometrix facilitates bibliometric analysis, using several APIs including the Dimensions Analytics API. Biblioshiny is a [Shiny](https://shiny.posit.co/) app, providing a web-interface for bibliometrix.

Previous Next

© Copyright 2026 Digital Science & Research Solutions, Inc. All Rights Reserved | https://www.dimensions.ai/
[About us](https://www.dimensions.ai/) · [Privacy policy](https://www.dimensions.ai/privacy/) · [Legal terms](https://www.dimensions.ai/website-terms/) Cookie Settings
