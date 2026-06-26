# Data sources and provenance

## Global Copper Deposit Dataset

Primary dataset:

- **Title:** Global Copper Deposit Dataset: A New Open-Source Database for Advanced Data Analysis and Exploration Targeting
- **Authors:** Bin Wang, Renguang Zuo, and Oliver P. Kreuzer
- **Journal:** Geoscience Data Journal
- **DOI:** https://doi.org/10.1002/gdj3.70040

The supplied source workbook is stored as `data/raw/Global_Copper_Deposit_Main.xlsx`. The exact frozen Stage 0 matrices and covariates used by HGCTM-S are stored in `data/processed/stage0/`.

## Macrostrat

Macrostrat was queried at deposit coordinates in the original workflow. The frozen response-derived table is `data/processed/stage0/macrostrat_lithology.csv`. The public platform and API documentation are available at:

- https://macrostrat.org/
- https://macrostrat.org/api/

The repository does not treat a coordinate query as confirmed deposit-scale host lithology.

## GLiM / LiMW

Independent regional lithology source:

- **Title:** The new global lithological map database GLiM: A representation of rock properties at the Earth surface
- **Authors:** Jens Hartmann and Nils Moosdorf
- **DOI:** https://doi.org/10.1029/2012GC004370
- **Dataset DOI:** https://doi.org/10.1594/PANGAEA.788537

The original polygon attributes, mapping metadata, and derived HGCTM-S classes are retained in the GLiM audit results and `data/covariates/`.

## Mineral nomenclature and family mapping

The primary notebook used IMA/RRUFF mineral-property data to support name normalisation and chemical-family assignment. The complete frozen mapping used by the analysis is:

`data/processed/stage0/mineral_to_family.csv`

RRUFF data portal:

- https://rruff.info/ima/

## Frozen cohorts

- Full model cohort: 1,335 deposits.
- Coordinate-valid cohort used for spatial and alternative-source experiments: 1,237 deposits.
- Placeholder-coordinate records excluded from coordinate-derived analyses: 98.
- Mineral-family vocabulary: 35 families.

The data audit and experiment-specific manifests are retained under `results/`.
