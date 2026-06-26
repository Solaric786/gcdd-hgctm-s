# Data directory

## `processed/stage0/`

Frozen model inputs exported by the Stage 0 workflow:

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

## Source-data note

The original GCDD workbook is not redistributed in this Git tree. Obtain it from the official source described in `../DATA_SOURCES.md` when reproducing the complete acquisition workflow.

## Manual-validation note

The completed 120-deposit manual host-lithology reference table and its analysis are not yet included. A sampling template retained within the GLiM audit outputs is not a completed validation dataset.
