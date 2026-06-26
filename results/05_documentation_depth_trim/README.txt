HGCTM documentation-depth trimmed Bernoulli sensitivity

Purpose
-------
This analysis tests whether the presence/absence results are driven by
a small set of exceptionally well-documented deposits.

Trimming
--------
Within each deposit type, deposits are ranked by:
1. mapped mineral-species count, descending;
2. present mineral-family count, descending;
3. Mindat ID, ascending.

ceil(10% × n_type) deposits are removed from every deposit type.

Model
-----
- Bernoulli HGCTM
- K = 7
- Macrostrat and GLiM
- equal lithology and age prior scales: 0.30/0.30
- seeds 42, 123, and 7
- 5,000 steps in full mode

Comparison
----------
Every trimmed run is aligned with the corresponding full-cohort
Bernoulli run from the previous presence/absence output archive.