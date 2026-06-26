# GCDD–HGCTM-S

Code, frozen model inputs, analysis notebooks, and summary outputs supporting the manuscript:

**Lithology-Dependent Mineral Assemblage Modes in Global Copper Deposits Revealed Using a Sparse Geological Context Topic Model**

Authors: Muhammad Atif Bilal and Kateryna Hlyniana.

- GitHub repository: https://github.com/Solaric786/gcdd-hgctm-s
- Current archived record: https://doi.org/10.5281/zenodo.19275907
- Repository version: `2.0.0-rc1`

## Release status

This repository contains the code and completed sensitivity analyses prepared for the major revision. It remains a release candidate rather than the final `v2.0.0` archive because the completed 120-deposit manual host-lithology validation table, its analysis notebook, and its statistical outputs are not yet included.

## Scientific scope

HGCTM-S is a sparse-deviation geological-context topic model for mineral-family records. It represents deposits as mixtures of latent assemblage modes and estimates how regional lithological context and broad geological age are associated with topic prevalence and mineral-family expression.

The revised repository separates:

1. the primary model and bootstrap analysis;
2. data and missingness audits;
3. independent GLiM regional-lithology extraction;
4. lithology-source and prior sensitivity;
5. presence/absence and documentation-depth sensitivity;
6. post hoc topic validation against deposit types;
7. leakage-safe geographic generalisation.

The removed supervised-classification workflow is not used as evidence.

## Repository structure

```text
.
├── notebooks/                 ordered analysis notebooks 00–08
├── data/
│   ├── processed/stage0/      frozen 1,335-deposit model inputs
│   └── covariates/            Macrostrat, GLiM, and combined assignments
├── results/                   summary tables, figures, and run manifests
├── scripts/                   repository validation utility
├── DATA_SOURCES.md
├── REPRODUCIBILITY.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
└── environment.yml
```

The original GCDD workbook is not redistributed in the Git tree. Full run-level arrays, loss traces, and compressed experimental bundles are intended for GitHub release assets and the Zenodo archive rather than ordinary Git history.

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
| 09 | **not yet included** | Completed manual host-lithology validation |

## Reproduction routes

### Frozen-input route

Use the files in `data/processed/stage0/` and execute notebooks in numerical order. This is the preferred route for reproducing the reported model inputs without repeating external database queries.

### Full acquisition route

Obtain the original GCDD source data from its official source, then follow the acquisition and preprocessing cells in the primary notebook. The primary and GLiM notebooks retain Kaggle-oriented input discovery. External data provenance is documented in `DATA_SOURCES.md`.

## Important interpretation limits

- Mineral-family counts represent recorded within-family species richness, not mineral abundance.
- Macrostrat and GLiM are regional coordinate-derived geological proxies, not verified deposit-scale host rocks.
- The `K=7` solution is the selected full-data interpretive resolution; training-only geographic prediction often favoured a smaller K.
- Geographic generalisation is continent-dependent rather than uniformly superior to a context-only baseline.
- Topic labels are dataset-derived, type-enriched assemblage modes rather than one-to-one genetic deposit classes.

## Verification

Run:

```bash
python scripts/verify_repository.py
```

The script checks required repository files, notebook JSON validity, cleared notebook outputs and execution counts, and prohibited superseded filenames. Warnings about the absent raw workbook and incomplete manual host-lithology validation are expected in this release candidate.

File hashes for the present Git-tree contents are provided in `checksums.sha256`.

## Citation

Use `CITATION.cff`. Before creating the final archive, verify whether the manuscript should cite the current Zenodo record or the DOI assigned to the new repository version.

## Licence

Original code and associated repository documentation are released under the MIT License; see `LICENSE`. Third-party source data and derived materials remain subject to the attribution and reuse conditions described in `DATA_SOURCES.md`.
