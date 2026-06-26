HGCTM strong geographic generalisation audit

- Fixed training-only LDA warm start per continent.
- HGCTM compared with context-only DM and global DM using the same
  complete held-out Dirichlet-Multinomial likelihood.
- LDA used for topic retention, not raw likelihood comparison.
- Optional training-only K=5..9 audit.
- Results must be described as post-selection geographic sensitivity,
  not untouched external model selection.