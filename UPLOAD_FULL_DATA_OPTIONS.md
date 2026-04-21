# Full data upload options

## Option 1: Git LFS
Use Git Large File Storage for the original CSV files.

Example commands:

```bash
git lfs install
git lfs track "*.csv"
git add .gitattributes
git add data/raw/ira/*.csv data/raw/brexit/*.csv
git commit -m "Add large datasets via Git LFS"
git push origin main
```

## Option 2: External data host
Upload the full datasets to Zenodo, OSF, or Figshare, then add links in the main README.

## Option 3: GitHub Releases
Attach compressed archives to a GitHub Release and document the download process.
