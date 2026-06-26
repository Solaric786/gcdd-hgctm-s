# Data directory

## `raw/`

`Global_Copper_Deposit_Main.xlsx` is the supplied GCDD source workbook used by the primary workflow. Its provenance and citation are documented in `../DATA_SOURCES.md`.

## `processed/stage0/`

Frozen model inputs exported by the original Stage 0 workflow:

- `X_family_copper.csv`
- `X_family_primary.csv`
- `covariates.csv`
- `deposit_completeness.csv`
- `lda_sweep_results.csv`
- `macrostrat_lithology.csv`
- `mineral_to_family.csv`

These files provide the preferred reproducibility entry point because they freeze the exact 1,335-deposit, 35-family representation used by the model.

## `covariates/`

Alternative regional lithology assignments used in the revision:

- original Macrostrat assignment;
- independent GLiM assignment;
- predefined Macrostrat–GLiM fallback assignment.

## `manual_validation/`

Contains the 120-deposit template only. It must be replaced by the completed manual reference table before the final release.
