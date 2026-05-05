# dimensions_api (official_dsl_docs_home)

Source URL: https://docs.dimensions.ai/dsl/
Local raw file: `references/canonical_sources/raw/dimensions_api/official_dsl_docs_home_dsl.html`

The Dimensions Search Language — DSL 2.14 documentation

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

- Release Notes and Deprecations

- Frequently Asked Questions

DSL

-

- The Dimensions Search Language

-

# The Dimensions Search Language 

## Version 2.14.0 

Welcome to the documentation of the Dimensions Search Language (DSL) project. The DSL enables users to perform analytics on the [Dimensions](https://www.dimensions.ai/) database.

This documentation contains high-level information about the project and its development, as well as the language’s features and usage. Please see the [APIs Homepage](https://www.dimensions.ai/dimensions-apis/) for more details about available API packages and subscriptions.

Note

The Dimensions Analytics API is subscription-only , so your Dimensions account needs to be activated for this service and subject to restrictions on use. Please send an email to supportapi @ dimensions . ai if you have any questions.

Important

The Dimensions Analytics API is not intended for bulk data or to power dashboards or other derivative products. The purpose of the API is to help support complex analytical tasks that could not otherwise be achieved through use of the Dimensions platform. For more information see also the page about Reasonable use .

Todo

Explore real-world applications of the API at the [Dimensions API Lab](https://digital-science.github.io/dimensions-api-lab/) , an open-source repository of Jupyter notebooks demonstrating how to carry out common scholarly analytics tasks e.g. building a citation network, doing a journal competitors analysis, tracking researchers’ affiliations over time etc..

## Contents: 

- Getting Started Checklist

- A Tour of the DSL

- A simple query

- The anatomy of a query

- search for source documents

- return information about documents

- Query Syntax

- Basic query structure

- Full-text Searching

- Field Searching

- Searching for Researchers

- Searching using concepts

- Searching using abstracts

- Returning results

- Formal language specification

- Functions Syntax

- Basic functions structure

- Function: classify

- Function: extract_affiliations

- Function: extract_concepts

- Function: extract_grants

- Expert Identification

- Step 1: Concept Extraction

- Step 2: Expert Identification

- Data Sources

- Publications

- Grants

- Patents

- Clinical Trials

- Policy Documents

- Datasets

- Source Titles

- Reports

- Researchers

- Organizations

- Funder Groups

- Research Org Groups

- Auxiliary Entities

- Literal Field Types

- Metadata API

- Example Queries and Results

- Minimal valid query

- Searching records

- Returning records

- Returning facets

- Naming/grouping results

- Limiting/paging results

- Indicators Aggregations

- API Access

- Getting an API Key

- Querying the API

- Python : raw access

- Python : Dimcli

- curl + jq

- PowerShell

- Postman

- Third-party Libraries and Tools

- Google Sheets / Excel Add-in

- Google Sheets Connector

- Excel Add-In

- Glossary

- Reasonable Use

- Technical Limits

- Release Notes and Deprecations

- Versions History

- Deprecations History

- Frequently Asked Questions

- 1. API Access & Support

- 2. Queries and Errors

- 3. Data Model

- 4. Logging and data retention

Next

© Copyright 2026 Digital Science & Research Solutions, Inc. All Rights Reserved | https://www.dimensions.ai/
[About us](https://www.dimensions.ai/) · [Privacy policy](https://www.dimensions.ai/privacy/) · [Legal terms](https://www.dimensions.ai/website-terms/) Cookie Settings
