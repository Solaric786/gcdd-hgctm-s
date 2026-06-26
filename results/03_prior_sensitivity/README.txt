HGCTM prior and lithology-class sensitivity at fixed K=7

This archive contains:
- 13 source/prior configurations;
- one or three seeds according to RUN_MODE;
- resumable per-run parameter archives and loss traces;
- fixed-scale and learned-scale results;
- frequency-weighted, unweighted, nonmissing, and strict-resolved effects;
- likelihood per deposit and per recorded mineral count;
- topic alignment and seed stability;
- rare-class warnings;
- reviewer-oriented decision tables.

For model fitting, the single raw GLiM evaporite observation is merged
into the broad other class. The raw class remains preserved in the audit
table.

The primary ratio is the class-frequency-weighted nonmissing lithology
effect divided by the corresponding nonmissing age effect.

The learned-scale model uses identical HalfNormal(0.5) hyperpriors for
lithology and age. Because the original omega_a parameter is retained,
the learned age scale must be interpreted jointly with omega_a.