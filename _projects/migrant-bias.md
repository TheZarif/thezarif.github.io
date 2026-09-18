---
title: "Migrant Bias in Web-Scale Search Datasets"
collection: projects
permalink: /projects/migrant-bias
date: 2025-01-01
type: "Research"
venue: "ECIR 2026 / public research release"
excerpt: "A published study and reproducible research release examining immigration narratives in MS MARCO search results."
tags:
  - Responsible AI
  - Information Retrieval
  - Migration Studies
  - Algorithmic Bias
---

This project examines how migrants, immigration systems, and related policies are represented in large-scale information retrieval (IR) datasets, with a particular focus on MS MARCO. Building on critical data studies and work on algorithmic bias, it asks how search results can encode and amplify specific framings of migrants. The work led to an [ECIR 2026 paper](https://doi.org/10.1007/978-3-032-21324-2_36) and a [public research release](https://github.com/TheZarif/msmarco-bias) with data, methods, and reproducible analysis.

## Research Questions

- Identify and categorize immigration-related queries and passages in MS MARCO and related IR benchmarks.
- Characterize how migrants and immigration issues are framed (e.g., security, economic, humanitarian, bureaucratic).
- Analyze how these framings might propagate bias into downstream IR and AI systems trained or evaluated on these datasets.
- Provide practical recommendations for building more representative and accountable IR benchmarks for migration-related topics.

## Methods

- Select immigration-related queries and retrieve candidate passages from MS MARCO.
- Compare BM25 results with passages reranked by BGE using an immigration-narrative frame taxonomy.
- Combine automated annotation with human validation and document annotation coverage.
- Report descriptive frame patterns while explicitly limiting comparisons where missing annotations could bias an inference.

## Status and Outputs

- **Status:** Published as an archival, non-commercial research release; no further annotation is planned for the released data.
- **Outputs:**
  - [How Information Retrieval Systems Construct and Amplify Immigration Narratives](https://doi.org/10.1007/978-3-032-21324-2_36), ECIR 2026.
  - [Data, analysis code, taxonomy, and research documentation](https://github.com/TheZarif/msmarco-bias).

If you are interested in this line of work or would like to collaborate on responsible IR and migration-focused datasets, feel free to reach out.
