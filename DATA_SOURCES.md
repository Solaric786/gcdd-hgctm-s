# Data sources and provenance

## Global Copper Deposit Dataset

Primary dataset:

- **Title:** Global Copper Deposit Dataset: A New Open-Source Database for Advanced Data Analysis and Exploration Targeting
- **Authors:** Bin Wang, Renguang Zuo, and Oliver P. Kreuzer
- **DOI:** 10.1002/gdj3.70040

The original GCDD workbook is not redistributed in this Git tree. Users reproducing the full acquisition workflow should obtain the source data from the official publication or associated data source and follow its reuse and attribution terms. The exact frozen Stage 0 matrices and covariates used by HGCTM-S are stored in `data/processed/stage0/`.

## Macrostrat

Macrostrat was queried at deposit coordinates in the original workflow. The frozen response-derived table is `data/processed/stage0/macrostrat_lithology.csv`.

The repository does not treat a coordinate query as confirmed deposit-scale host lithology.

## GLiM / LiMW

Independent regional lithology source:

- **Title:** The new global lithological map database GLiM: A representation of rock properties at the Earth surface
- **Authors:** Jens Hartmann and Nils Moosdorf
- **Article DOI:** 10.1029/2012GC004370
- **Dataset DOI:** 10.1594/PANGAEA.788537

The mapping metadata and derived HGCTM-S classes are retained in the GLiM audit results and `data/covariates/`.

## Mineral nomenclature and family mapping

The primary notebook used IMA/RRUFF mineral-property information to support name normalisation and chemical-family assignment. The complete frozen mapping used by the analysis is:

`data/processed/stage0/mineral_to_family.csv`

## Frozen cohorts

- Full model cohort: 1,335 deposits.
- Coordinate-valid cohort used for spatial and alternative-source experiments: 1,237 deposits.
- Placeholder-coordinate records excluded from coordinate-derived analyses: 98.
- Mineral-family vocabulary: 35 families.

The data audit and experiment-specific manifests are retained under `results/`.

## Reuse

The MIT License covers original code and associated repository documentation. It does not replace the licences, attribution requirements, or other terms applicable to third-party source data.
