# F1 Driver-Season Clustering: DBSCAN vs GMM

TP Machine Learning, Option 4 (Clustering). ISSAT Sousse, 2026–2027.

We group Formula 1 driver-seasons (2014–2025) by performance profile with **DBSCAN** and a **Gaussian Mixture Model**, then compare the two algorithms.

## Dataset

- **Name:** [Formula 1 Race Data](https://www.kaggle.com/datasets/jtrotman/formula-1-race-data) by jtrotman (Kaggle)
- **Version used:** race data from 1950 to 2026, last race included: 2026 Race 21, Las Vegas Grand Prix
- **Tables used** (in `data/raw/`): `races`, `results`, `qualifying`, `drivers`, `constructors`, `driver_standings`
- **Processed data** (in `data/processed/`): `driver_seasons.csv` (246 driver-seasons) and `driver_seasons_scaled.csv` (the algorithms' input)

## Project structure

```
data/raw/          original CSVs, never modified
data/processed/    clean tables created by the notebook
notebooks/         f1_clustering.ipynb
figures/           plots used in the presentation
presentation/      slides
```

## How to run

```
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
```

Open `notebooks/f1_clustering.ipynb` and run **Restart & Run All**.