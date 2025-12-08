---
title: "Migrant Bias in Web-Scale Search Datasets"
collection: projects
permalink: /projects/migrant-bias
date: 2025-01-01  # choose any approximate start date (YYYY-MM-DD)
type: "Research"
venue: "In progress"
excerpt: "Studying how immigration-related queries and passages are framed in large-scale IR benchmarks (e.g., MS MARCO) to uncover biases in how migrants and immigration are represented."
tags:
  - Responsible AI
  - Information Retrieval
  - Migration Studies
  - Algorithmic Bias
image: /images/projects/migrant-bias.png   # optional; add image or remove this line
link: https://github.com/your-username/msmarco-bias  # optional, update or delete
---

This project examines how migrants, immigration systems, and related policies are represented in large-scale information retrieval (IR) datasets, with a particular focus on MS MARCO and immigration-related queries and passages. Building on critical data studies and work on algorithmic bias, the project asks how seemingly “neutral” benchmarks encode specific framings of migrants (e.g., as risks, workers, students, or burdens).

## Goals

- Identify and categorize immigration-related queries and passages in MS MARCO and related IR benchmarks.
- Characterize how migrants and immigration issues are framed (e.g., security, economic, humanitarian, bureaucratic).
- Analyze how these framings might propagate bias into downstream IR and AI systems trained or evaluated on these datasets.
- Provide practical recommendations for building more representative and accountable IR benchmarks for migration-related topics.

## Methods

- Use keyword- and embedding-based retrieval to filter immigration-related queries and passages.
- Develop a taxonomy of immigration-related frames (drawing on migration studies and framing theory).
- Apply a combination of manual coding and LLM-assisted annotation to label frames at scale.
- Quantitatively analyze frame distributions and temporal patterns, and link them to broader discourses about migrants and immigration.
- Explore how biased framing in benchmarks can affect model behavior in retrieval and ranking tasks.

## Status and Outputs

- **Status:** Ongoing research project.
- **Planned outputs:**
  - A research paper on bias and framing in MS MARCO immigration content (target: IR / Web / Responsible AI venues).
  - Reusable annotated subsets and frame taxonomies for researchers working at the intersection of IR and migration studies.
  - Methodological guidelines for auditing benchmark datasets for representational harms affecting migrants and other marginalized groups.

If you are interested in this line of work or would like to collaborate on responsible IR and migration-focused datasets, feel free to reach out.
