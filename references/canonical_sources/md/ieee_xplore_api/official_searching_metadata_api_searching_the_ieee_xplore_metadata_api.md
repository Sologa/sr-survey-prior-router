# ieee_xplore_api (official_searching_metadata_api)

Source URL: https://developer.ieee.org/docs/read/Searching_the_IEEE_Xplore_Metadata_API
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/ieee_xplore_api/official_searching_metadata_api_searching_the_ieee_xplore_metadata_api.html`

IEEE Xplore - API Query Basics

IEEE Xplore

- [Sign In](https://developer.ieee.org/login/login?r=https%3A%2F%2Fdeveloper.ieee.org%2Fdocs%2Fread%2FSearching_the_IEEE_Xplore_Metadata_API&h=e9136bad6e018542a74d4e5c3c2b4109)

- [Register](https://developer.ieee.org/member/register)

- Previous: [API Use Cases](https://developer.ieee.org/docs/read/IEEE_Xplore_Metadata_API_Overview)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [Search Parameters](https://developer.ieee.org/docs/read/Metadata_API_details)

# API Query Basics

## Structuring a Query:

The general structure for a search query is: https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey=

Additional parameters may be included by appending ¶meter for each additional parameter.

All full-text artilcle retrieval (Ex: Open Access) requires article number as a parameter.

The default response is JSON. For XML append to the request. For JSON, append URL with callback=${somevalue} .

NOTE:

- The API key you received after completing the registration process MUST be appended to EVERY query. You can find your API key under My Account.

- All parameter values should be URL encoded.

- The order of parameters does not matter.

- The Metadata API returns all available metadata records in the IEEE Xplore Digital Library. This may result in retrieval of metadata outside of an existing individual or institutional subscription to IEEE Xplore.

version 25 as of 6 years ago by Manny Rechani

- Previous: [API Use Cases](https://developer.ieee.org/docs/read/IEEE_Xplore_Metadata_API_Overview)

- Up: [Currently Available APIs](https://developer.ieee.org/docs/read/Home)

- Next: [Search Parameters](https://developer.ieee.org/docs/read/Metadata_API_details)

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
