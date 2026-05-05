# dimensions_api (official_reasonable_use_corrected)

Source URL: https://docs.dimensions.ai/dsl/usagepolicy.html
Local raw file: `references/canonical_sources/raw/dimensions_api/official_reasonable_use_corrected_usagepolicy.html.html`

Reasonable Use — DSL 2.14 documentation

DSL

- Getting Started Checklist

- A Tour of the DSL

- Query Syntax

- Functions Syntax

- Expert Identification

- Data Sources

- Example Queries and Results

- API Access

- Google Sheets / Excel Add-in

- Glossary

- Reasonable Use

- Technical Limits

- Release Notes and Deprecations

- Frequently Asked Questions

DSL

-

- Reasonable Use

-

# Reasonable Use 

The purpose of the API is to help support complex analytical tasks that could not otherwise be achieved through use of the Dimensions platform.

It is not intended to be used to create local copies of the Dimensions data for use as an alternative to the API, which should remain as the primary source of the data. You should limit your use to what is necessary for the particular analytical task you are performing, not multiple or undefined use cases, and never in a way which may have an adverse impact on the performance or others’ use of the API.

If you require access to substantial volumes of Dimensions data, please let us know so that we can advise on the most appropriate means of getting that access.

We reserve the right to impose such limits on the API as we consider are reasonable. Please also make sure you comply with the other terms of your Dimensions subscription.

## Technical Limits 

To ensure good performance for all API users, the following general limits apply and cannot be modified:

-
max. 30 requests per IP address per minute

-
max. number of items used in in filter clause: up to 400 , example: search publications where id in [...]

-
max. number of boolean filter conditions: up to 100 , example: search publications where field1 = value and field2 = value

-
max. number of boolean full text clauses: up to 100 , example: search publications in authors for "\"Alan Turing\" OR \"Stephen Hawking\""

-
max. number of records that can be returned in a single query: 1,000

-
max. number of records than can be returned for a single search, using pagination (limit and skip), with max. 1,000 records per page: 50,000

-
max. number of records that can be returned when returning facets: 1,000 (no pagination possible)

Previous Next

© Copyright 2026 Digital Science & Research Solutions, Inc. All Rights Reserved | https://www.dimensions.ai/
[About us](https://www.dimensions.ai/) · [Privacy policy](https://www.dimensions.ai/privacy/) · [Legal terms](https://www.dimensions.ai/website-terms/) Cookie Settings
