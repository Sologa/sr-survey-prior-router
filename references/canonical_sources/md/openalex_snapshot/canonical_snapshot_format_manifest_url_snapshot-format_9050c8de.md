# openalex_snapshot (canonical_snapshot_format_manifest_url)

Source URL: https://developers.openalex.org/download/snapshot-format
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/openalex_snapshot/canonical_snapshot_format_manifest_url_snapshot-format_9050c8de.html`

Snapshot data format - OpenAlex Developers

Skip to main content

OpenAlex Developers home page

Search...

⌘ K

##### Data Downloads

-

Overview

-

Snapshot data format

-

Download to your machine

-

OpenAlex CLI

-

Full-text PDFs

-

Download Changefiles

-

OpenAlex Developers home page

Search...

⌘ K

Search...

Navigation

Data Downloads

Snapshot data format

Guides

API Reference

Data Downloads

Guides

API Reference

Data Downloads

Data Downloads

# Snapshot data format

Copy page

Where the OpenAlex data lives and how it’s structured

Copy page

## Documentation Index

Fetch the complete documentation index at: [https://developers.openalex.org/llms.txt](https://developers.openalex.org/llms.txt)

Use this file to discover all available pages before exploring further.

All OpenAlex data is stored in [Amazon S3](https://aws.amazon.com/s3/) in the [openalex](https://openalex.s3.amazonaws.com/browse.html) bucket. The data files are gzip-compressed [JSON Lines](https://jsonlines.org/) — one entity per line.

##
​

Bucket structure
The bucket contains one prefix (folder) for each entity type:

Entity

S3 prefix

Browse

Works

/data/works/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/works/)

Authors

/data/authors/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/authors/)

Sources

/data/sources/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/sources/)

Institutions

/data/institutions/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/institutions/)

Topics

/data/topics/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/topics/)

Domains

/data/domains/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/domains/)

Fields

/data/fields/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/fields/)

Subfields

/data/subfields/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/subfields/)

Publishers

/data/publishers/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/publishers/)

Funders

/data/funders/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/funders/)

Concepts

/data/concepts/

[Browse](https://openalex.s3.amazonaws.com/browse.html#data/concepts/)

Records are partitioned by updated_date . Within each entity type, files are further prefixed by date. For example, an Author with updated_date of 2024-01-15 lives under:

/data/authors/updated_date=2024-01-15/

Each partition contains multiple gzip files, each under 2 GB.

##
​

Size
The gzip-compressed snapshot is approximately 330 GB and decompresses to about 1.6 TB .

##
​

Entity schemas
The structure of each entity type matches the API response format:

## Works

## Authors

## Sources

## Institutions

## Topics

## Publishers

API-only fields: Some Work properties are only available through the API and not included in the snapshot. For example, content_url — use the content endpoint directly with work IDs from the snapshot.

##
​

Keeping your snapshot up to date
The updated_date partitions make incremental updates straightforward. Unlike dated snapshots that each contain the full dataset, each partition contains only the records that last changed on that date.

###
​

How partitions work
Imagine launching OpenAlex with 1,000 Authors, all created on 2024-01-01:

/data/authors/ ├── manifest └── updated_date=2024-01-01 [1000 Authors] ├── 0000_part_00.gz └── ...

If we update 50 of those Authors on 2024-01-15, they move out of the old partition and into the new one:

/data/authors/ ├── manifest ├── updated_date=2024-01-01 [950 Authors] │ └── ... └── updated_date=2024-01-15 [50 Authors] └── ...

If we also discover 50 new Authors, they go into the same new partition:

/data/authors/ ├── manifest ├── updated_date=2024-01-01 [950 Authors] │ └── ... └── updated_date=2024-01-15 [100 Authors] └── ...

So if you made your snapshot copy on 2024-01-01, you only need to download updated_date=2024-01-15 to get everything that changed or was added since then.

To update a snapshot copy that you created or updated on date X , insert or update the records in partitions where updated_date > X .

You never need to re-download a partition you already have. Anything that changed has moved to a newer partition.

##
​

The manifest file
Each entity type has a manifest file that lists all data files. When we start writing a new updated_date partition, we delete the manifest. When we finish, we recreate it with the new files included. So if the manifest is present, all data files are complete. The file uses [Redshift manifest](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) format. To use it for incremental updates:

1

Download the manifest

aws s3 cp s3://openalex/data/authors/manifest ./manifest --no-sign-request

2

Check for new partitions

Get the file list from the url property of each item in the entries list. Identify any updated_date partitions you haven’t seen before.

3

Download new partitions

Download objects with new updated_date values.

4

Verify consistency

Download the manifest again. If it hasn’t changed since step 1, no records moved between partitions during your download.

5

Load the data

Decompress the files and parse one JSON entity per line. Insert or update into your database using each entity’s ID as the primary key.

If you have an existing data pipeline, these details may be all you need. For step-by-step download instructions, see Download to your machine .

Previous

Download to your machine Get the OpenAlex snapshot files onto your local machine using the AWS CLI

Next

⌘ I

[x](https://x.com/openalex_org) [github](https://github.com/ourresearch)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=openalex) [This documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=openalex)

On this page

- Bucket structure

- Size

- Entity schemas

- Keeping your snapshot up to date

- How partitions work

- The manifest file
