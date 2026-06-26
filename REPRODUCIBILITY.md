# Reproducibility guide

## Recommended execution sequence

1. `00_data_and_missingness_audit.ipynb`
2. `01_primary_hgctm_s_model.ipynb`
3. `02_glim_lithology_audit.ipynb`
4. `03_lithology_source_sensitivity.ipynb`
5. `04_prior_and_lithology_class_sensitivity.ipynb`
6. `05_presence_absence_sensitivity.ipynb`
7. `06_documentation_depth_trimmed_bernoulli.ipynb`
8. `07_topic_validation_against_deposit_types.ipynb`
9. `08_strong_geographic_generalisation.ipynb`
10. `09_manual_host_lithology_validation.ipynb` — still required

## Environment

The completed revision experiments recorded the following core environment:

- Python 3.12.13
- NumPy 2.4.6
- pandas 2.3.3
- PyTorch 2.10.0+cpu
- Pyro 1.9.1

`requirements.txt` fixes these core versions and constrains the remaining dependencies. Platform-specific geospatial packages may require conda-forge.

## Kaggle execution

The notebooks were developed as Kaggle workflows and include input discovery under `/kaggle/input` and output writing under `/kaggle/working`. The release assets should be attached to the Kaggle notebook or unpacked as input datasets using their original archive names.

## Local execution

For local execution, create the environment and expose the repository data and prior outputs using repository-relative paths or symbolic links. Because several notebooks retain Kaggle-compatible discovery logic, the least invasive local setup is to create an `inputs/` directory containing unpacked release assets and adapt the input-root cell at the beginning of each notebook.

## Dependency chain

- Notebook 01 creates the primary HGCTM-S result bundle required by Notebook 07.
- Notebook 02 creates the three lithology-source covariate files required by Notebooks 03–08.
- Notebook 05 produces the full Bernoulli models used as references in Notebook 06.
- Notebook 04 and/or the release assets provide the fixed original Macrostrat run used by the strong geographic audit.

## Randomness and fitting

The revision experiments use seeds 42, 123, and 7 where stated. Exact settings and run counts are stored in each experiment's `run_manifest.json`. Do not change K, prior scales, optimisation steps, class handling, or the training-only warm-start rules when reproducing manuscript values.

## Public Git tree versus release assets

The Git tree contains notebooks, frozen inputs, summary tables, figures, and manifests. Full `.npz`, `.npy`, loss-trace, and run-summary collections are stored as compressed release assets to avoid cluttering Git history.

## Known incomplete component

The 120-deposit manual host-lithology sample is present only as a template. The completed reference table, analysis notebook, and statistical outputs must be added before the final `v2.0.0` tag.
