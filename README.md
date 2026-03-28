# GCDD-HGCTM-S

Code and reproducible workflow for the HGCTM-S analysis of the Global Copper Deposit Database (GCDD).
Repository prepared for research transparency and peer review. The shared notebook is a cleaned public version of the Kaggle workflow.

## Repository contents

- `gcdd-hgctm-s_github_clean.ipynb` : cleaned notebook prepared for public GitHub sharing
- `LICENSE : temporary rights notice for review version
- `.gitignore` : Python ignore rules
- `requirements.txt` : basic Python package requirements
- `DATA_SOURCES.md` : summary of main input datasets, generated files, and execution environment notes

## Notes

- This notebook was cleaned for public release.
- Saved outputs and execution counts were removed.
- Some cells still use Kaggle-specific paths such as `/kaggle/input/...` and `/kaggle/working/...`.
- If you run the notebook outside Kaggle, those paths should be updated.

## Reproducibility

The notebook reflects the research workflow used for the HGCTM-S study.
External data sources and environment-specific settings should be documented further as the repository develops.

## Data and execution notes

This repository currently provides the public notebook and basic environment requirements.

### Data sources
The workflow uses data prepared and accessed in the Kaggle environment. Some inputs may come from public external sources and some intermediate files may be written to the Kaggle working directory during execution.

### Kaggle paths
Several cells use Kaggle-specific paths such as `/kaggle/input/...` and `/kaggle/working/...`.

In Kaggle:
- input datasets are typically mounted under `/kaggle/input/`
- generated files are typically written to `/kaggle/working/`

If the notebook is executed outside Kaggle, these paths should be replaced with local paths or repository-relative paths.

### Running the notebook
The notebook is currently shared in a form suitable for code inspection and research transparency.
A fully refreshed execution-ready version can be prepared after final path standardization and data-access documentation.

### Data availability
Readers should consult the associated manuscript and linked public data sources for dataset descriptions, provenance, and any access conditions.

## How to use this repository

1. Review the notebook `gcdd-hgctm-s_github_clean.ipynb`.
2. Install the basic Python dependencies listed in `requirements.txt`.
3. Prepare access to the required datasets in the Kaggle environment or replace Kaggle-specific paths with your local paths.
4. Execute the notebook step by step in the appropriate environment.
5. Check generated outputs and intermediate files in the working directory as needed.

## Citation

If this repository is used in academic work, please cite the associated paper when available.
