# Entropy Dynamics as an Early-Warning Signal for Structural Reorganization

This is a **lightweight GitHub-ready repository package** prepared to stay below common browser upload limits.

## What is included

- blind-review manuscript PDF and LaTeX source in `docs/`
- small sample datasets in `data/samples/`
- dataset inventory in `metadata/`
- helper script in `scripts/`

## Why the full data are not included here

The original CSV files are too large for simple browser-based upload workflows that reject files above roughly 25 MB.
For the full datasets, use one of these options:

1. **Git LFS** for large CSV files
2. **GitHub Releases** and link them in the README
3. **Zenodo / OSF / Figshare** for archival hosting, then link from the repository

## Suggested public repository structure

```text
.
├── data/
│   └── samples/
│       ├── brexit/
│       └── ira/
├── docs/
├── metadata/
├── scripts/
├── .gitignore
├── README.md
└── UPLOAD_FULL_DATA_OPTIONS.md
```

## Included samples

- `data/samples/ira/IRAhandle_tweets_1.csv` — first 1000 rows
- `data/samples/ira/IRAhandle_tweets_2.csv` — first 1000 rows
- `data/samples/ira/IRAhandle_tweets_3.csv` — first 1000 rows
- `data/samples/brexit/tcat_brexit_train_sample.csv` — first 1000 data rows

## Recommendation

Upload this lightweight package to GitHub now.
Keep the full raw datasets outside the main repository unless you use Git LFS or an external archival host.
