#!/usr/bin/env python3
"""Validate the public HGCTM-S repository package."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "DATA_SOURCES.md",
    "REPRODUCIBILITY.md",
    "requirements.txt",
    "environment.yml",
    "data/README.md",
    "data/processed/stage0/X_family_copper.csv",
    "data/processed/stage0/X_family_primary.csv",
    "data/processed/stage0/covariates.csv",
    "data/processed/stage0/deposit_completeness.csv",
    "data/processed/stage0/lda_sweep_results.csv",
    "data/processed/stage0/macrostrat_lithology.csv",
    "data/processed/stage0/mineral_to_family.csv",
    "data/covariates/covariates_lithology_A_macrostrat_original.csv",
    "data/covariates/covariates_lithology_B_glim_only.csv",
    "data/covariates/covariates_lithology_C_macrostrat_glim_combined.csv",
    "data/covariates/phase1b_source_and_mapping_metadata.json",
    "notebooks/00_data_and_missingness_audit.ipynb",
    "notebooks/01_primary_hgctm_s_model.ipynb",
    "notebooks/02_glim_lithology_audit.ipynb",
    "notebooks/03_lithology_source_sensitivity.ipynb",
    "notebooks/04_prior_and_lithology_class_sensitivity.ipynb",
    "notebooks/05_presence_absence_sensitivity.ipynb",
    "notebooks/06_documentation_depth_trimmed_bernoulli.ipynb",
    "notebooks/07_topic_validation_against_deposit_types.ipynb",
    "notebooks/08_strong_geographic_generalisation.ipynb",
    "notebooks/README.md",
]

required_directories = [
    "data/processed/stage0",
    "data/covariates",
    "notebooks",
    "results",
    "scripts",
]

prohibited_names = {
    "gcdd-hgctm-s_github_clean.ipynb",
    "HGCTM_Corrected_Geographic_Holdout_and_Unknown_Audit_K7.ipynb",
    "HGCTM_Topic_Validation_Against_Deposit_Types_K7.ipynb",
    "table2_dominant_topic_accuracy.csv",
    "table4_rf_cv_summary.csv",
}

errors = []
warnings = []

for rel in required_files:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for rel in required_directories:
    if not (ROOT / rel).is_dir():
        errors.append(f"missing required directory: {rel}")

for path in ROOT.rglob("*"):
    if path.name in prohibited_names:
        errors.append(f"superseded or excluded file present: {path.relative_to(ROOT)}")

notebook_dir = ROOT / "notebooks"
if notebook_dir.is_dir():
    for path in notebook_dir.glob("*.ipynb"):
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            cells = notebook.get("cells")
            if not isinstance(cells, list):
                raise ValueError("missing or invalid cells list")

            for index, cell in enumerate(cells):
                if cell.get("cell_type") != "code":
                    continue
                if cell.get("execution_count") is not None:
                    errors.append(
                        f"notebook execution count not cleared: "
                        f"{path.name}, cell {index}"
                    )
                if cell.get("outputs"):
                    errors.append(
                        f"notebook output not cleared: {path.name}, cell {index}"
                    )
        except Exception as exc:
            errors.append(f"invalid notebook JSON: {path.name}: {exc}")

primary = ROOT / "notebooks/01_primary_hgctm_s_model.ipynb"
if primary.is_file():
    text = primary.read_text(encoding="utf-8")
    removed_markers = [
        "CELL 29 — Continent holdout",
        "CELL 32 — Negative controls",
        "CELL 33 — Supervised classification",
        "Figure 4: Stability + validation panel",
    ]
    for marker in removed_markers:
        if marker in text:
            errors.append(
                f"removed workflow marker still present in primary notebook: {marker}"
            )

manual_completed = (
    ROOT
    / "data/manual_validation/manual_host_lithology_validation_120_completed.csv"
)
manual_notebook = ROOT / "notebooks/09_manual_host_lithology_validation.ipynb"

if not manual_completed.is_file() or not manual_notebook.is_file():
    warnings.append(
        "manual host-lithology validation is not yet complete; "
        "add the completed table and notebook before the final archived release"
    )

raw_workbook = ROOT / "data/raw/Global_Copper_Deposit_Main.xlsx"
if not raw_workbook.exists():
    warnings.append(
        "raw GCDD workbook is not included; this is acceptable when redistribution "
        "permission has not been confirmed"
    )

print("HGCTM-S repository validation")
print(f"Root: {ROOT}")

if warnings:
    print("\nWarnings:")
    for message in warnings:
        print(f"  - {message}")

if errors:
    print("\nErrors:")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)

print("\nCore repository checks passed.")
