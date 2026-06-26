# GCDD–HGCTM-S

Code, frozen model inputs, analysis notebooks, and summary outputs supporting the manuscript:

**Lithology-Dependent Mineral Assemblage Modes in Global Copper Deposits Revealed Using a Sparse Geological Context Topic Model**

Authors: Muhammad Atif Bilal and Kateryna Hlyniana.

- GitHub repository: https://github.com/Solaric786/gcdd-hgctm-s
- Current archived record: https://doi.org/10.5281/zenodo.19275907
- Release-candidate version in this package: `2.0.0-rc1`

## Release status

This directory is prepared for the major-revision repository update. It should not be tagged as the final `v2.0.0` release until the completed 120-deposit manual host-lithology validation table, analysis notebook, and outputs have been added.

## Scientific scope

HGCTM-S is a sparse-deviation, geological-context topic model for mineral-family records. It represents deposits as mixtures of latent assemblage modes and estimates how regional lithological context and broad geological age are associated with topic prevalence and mineral-family expression.

The revised repository separates:

1. the primary model and bootstrap analysis;
2. data and missingness audits;
3. independent GLiM regional-lithology extraction;
4. lithology-source and prior sensitivity;
5. presence/absence and documentation-depth sensitivity;
6. post hoc topic validation against deposit types;
7. leakage-safe geographic generalisation.

The removed supervised/classifier workflow is not used as evidence.

## Repository structure

```text
.
├── notebooks/                 ordered analysis notebooks
├── data/
│   ├── raw/                   supplied GCDD workbook
│   ├── processed/stage0/      frozen 1,335-deposit model inputs
│   ├── covariates/            Macrostrat, GLiM, and combined assignments
│   └── manual_validation/     template; completion still required
├── results/                   summary tables, figures, and run manifests
├── scripts/                   repository validation utility
├── DATA_SOURCES.md
├── REPRODUCIBILITY.md
├── CHANGELOG.md
├── CITATION.cff
├── requirements.txt
└── environment.yml
```

Full run-level arrays, loss traces, and compressed experimental bundles are intended for the GitHub release assets and Zenodo archive rather than the normal Git tree.

## Notebook order

| Order | Notebook | Purpose |
|---|---|---|
| 00 | `00_data_and_missingness_audit.ipynb` | Cohort flow, unknown/other classes, coordinate audit |
| 01 | `01_primary_hgctm_s_model.ipynb` | Primary model, model ladder, bootstrap, missingness, ontology |
| 02 | `02_glim_lithology_audit.ipynb` | Independent GLiM extraction and comparison |
| 03 | `03_lithology_source_sensitivity.ipynb` | Macrostrat, GLiM, combined-source comparison |
| 04 | `04_prior_and_lithology_class_sensitivity.ipynb` | Equal, reversed, and learned prior scales |
| 05 | `05_presence_absence_sensitivity.ipynb` | Binary-DM and Bernoulli sensitivity |
| 06 | `06_documentation_depth_trimmed_bernoulli.ipynb` | Upper-10% documentation trim |
| 07 | `07_topic_validation_against_deposit_types.ipynb` | Post hoc external geological validation |
| 08 | `08_strong_geographic_generalisation.ipynb` | Context-only/global baselines and training-only K audit |
| 09 | **to be added** | Completed manual host-lithology validation |

## Reproduction routes

### Frozen-input route

Use the files in `data/processed/stage0/` and execute notebooks in numerical order. This is the preferred route for reproducing the reported model inputs without repeating external database queries.

### Full acquisition route

The primary and GLiM notebooks contain the original Kaggle-oriented acquisition steps. External data access, map versions, and provenance are documented in `DATA_SOURCES.md`.

## Important interpretation limits

- Mineral-family counts are recorded within-family species richness, not mineral abundance.
- Macrostrat and GLiM are regional coordinate-derived geological proxies, not verified deposit-scale host rocks.
- The `K=7` solution is the selected full-data interpretive resolution; training-only geographic prediction often favoured a smaller K.
- Geographic generalisation is continent-dependent rather than uniformly superior to a context-only baseline.
- Topic labels are dataset-derived, type-enriched assemblage modes rather than one-to-one genetic deposit classes.

## Verification

Run:

```bash
python scripts/verify_repository.py
```

The script checks required files, notebook JSON validity, prohibited superseded filenames, and package hashes. A warning about manual validation is expected until Notebook 09 and the completed table are added.

## Citation

Use `CITATION.cff`. Before final release, verify whether the Zenodo DOI above remains the correct concept DOI or whether the manuscript should cite the DOI assigned to the new repository version.

## Licence

The existing public repository uses an all-rights-reserved review notice. A final code and data licence has not been selected in this release candidate. See `LICENSE_DECISION_REQUIRED.md`.
