HGCTM presence/absence sensitivity at fixed K=7

Purpose
-------
This analysis tests whether the reported assemblage modes and the
lithology-to-age effect depend on repeated mineral-species counts within
the 35 mineral families.

Data
----
The same 1,237 coordinate-valid deposits and 35 families are used.
Every positive family count is converted to one.

Models
------
1. Binary Dirichlet-Multinomial:
   closest architectural comparison with the submitted count model.

2. Bernoulli HGCTM:
   natural presence/absence formulation; every deposit contributes
   exactly 35 family-level Bernoulli observations.

Design
------
- Macrostrat and GLiM lithology
- original and equal-high prior settings
- three seeds
- K=7
- 24 fits in full mode

The optional prior-sensitivity output enables direct comparison with the
matching count-based run for topic alignment, top-family overlap, mixture
agreement, and effect-ratio change.