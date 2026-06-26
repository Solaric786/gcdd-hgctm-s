# Changelog

## 2.0.0-rc1 — major-revision release candidate

### Added

- data-flow and unknown-class audit;
- independent GLiM regional-lithology extraction;
- Macrostrat, GLiM, and combined-source sensitivity;
- equal-low, equal-high, reversed, and learned prior-scale experiments;
- binary Dirichlet–Multinomial and Bernoulli presence/absence analyses;
- documentation-depth trimming;
- post hoc topic validation against independent deposit-type labels;
- strong leave-one-continent-out analysis with global and context-only Dirichlet–Multinomial baselines;
- training-only K sensitivity;
- frozen Stage 0 model inputs;
- experiment manifests, summary tables, and figures.

### Changed

- reorganised the repository into ordered notebooks, data, results, and documentation;
- revised topic terminology to assemblage modes and type-enriched associations;
- separated full-data interpretive K selection from geographic predictive K sensitivity;
- distinguished regional lithological context from verified deposit-scale host rock;
- replaced unpinned basic requirements with a documented environment.

### Removed from evidential workflow

- supervised classification and classifier-based negative controls;
- the earlier continent-holdout implementation;
- direct comparison of raw scikit-learn LDA likelihood with HGCTM Dirichlet–Multinomial likelihood;
- duplicate earlier topic-validation heatmap notebook.

### Still required before final 2.0.0

- completed 120-deposit manual host-lithology reference table;
- manual-validation notebook and outputs;
- final licence decision;
- final Zenodo version DOI check.
