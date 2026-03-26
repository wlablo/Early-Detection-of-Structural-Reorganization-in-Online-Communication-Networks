# Higgs Communication Network Analysis

Code and project structure for reproducing the analyses from the manuscript:

**Early Detection of Structural Reorganization in Online Communication Networks: A Multiplex Graph-State Approach**

## Structure

- `src/` — reusable analysis functions
- `run_analysis.py` — entry point for running the pipeline
- `data/raw/` — raw input data (place `higgs-activity_time.txt` or `.gz` here)
- `data/processed/` — processed outputs
- `figures/` — generated and manuscript figures
- `notebooks/` — optional exploratory notebooks

## Expected input

Place the Higgs activity file in `data/raw/`:

- `higgs-activity_time.txt`
- or `higgs-activity_time.txt.gz`

The script expects columns:

`timestamp user_a user_b interaction_type`

where interaction types can include `RT`, `MT`, and `RE`.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
```

## Run

```bash
python run_analysis.py --input data/raw/higgs-activity_time.txt.gz --window-hours 1
```

## Outputs

The pipeline computes per-window:

- von Neumann entropy
- quantum Jensen–Shannon divergence (QJSD)
- fidelity
- a simple curvature proxy derived from second differences in QJSD

and writes:

- processed CSV files to `data/processed/`
- diagnostic plots to `figures/`

## Notes

This repository is a clean, reproducible project skeleton for the article workflow. Before public release, verify the exact preprocessing and parameter settings against the final manuscript.
