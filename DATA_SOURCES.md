# Data Sources

This file summarizes the main datasets and generated files used in the HGCTM-S workflow.

## Main input data

- **Global Copper Deposit Database**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/katerynaglin/global-copper-deposit-dataset-main`
  - Role: main deposit database used for analysis

- **HGCTM stage 0 data**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/katerynaglin/hgctm-stage0`
  - Role: intermediate or prepared data for the workflow

- **HGCTM results**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/katerynaglin/hgctm-results`
  - Role: stored results used in later stages of analysis

- **HGCTM results bundle**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/katerynaglin/hgctm-results-bandle`
  - Role: archived or bundled result files

- **LDA sweep results**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/katerynaglin/hgctm-stage0/lda_sweep_results.csv`
  - Role: topic-model sweep or model-selection results

- **IMA / RRUFF mineral properties data**
  - Kaggle path used in the notebook: `/kaggle/input/datasets/lsind18/ima-database-of-mineral-properties/RRUFF_Export_20230608_052338.csv`
  - Role: mineral reference data used in the workflow

## Generated working files

The notebook also writes intermediate or output files to `/kaggle/working/`, including:

- `X_family_copper.csv`
- `X_family_primary.csv`
- `covariates.csv`
- `deposit_completeness.csv`
- `macrostrat_lithology.csv`
- `mineral_to_family.csv`
- `resolved_lithology_robustness_check.csv`
- `lda_sweep_results.csv`

## Generated figures

Figures are written to `/kaggle/working/figures/`, including:

- `fig1_topic_heatmap.png`
- `fig2_tau_ranking.png`
- `fig3_litho_deviations.png`
- `fig4_validation_panel.png`
- `fig5_global_map.png`

## Environment note

The notebook was originally developed in Kaggle and uses Kaggle-specific paths such as `/kaggle/input/` and `/kaggle/working/`.  
If the workflow is executed outside Kaggle, these paths should be updated accordingly.
