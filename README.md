# HDB Resale Prices

```
pip install -r requirements.txt
```

This is a project on HDB Resale Housing prices in Singapore. The dataset can be found [here](https://data.gov.sg/collections/189/view).
All the code can be found in [notebook](https://github.com/jeslyztaz/hdb-resale-prices/blob/master/notebooks/data%20cleaning%20%2B%20postgresql.ipynb))
For a detailed analysis, please refer to this [writeup](https://github.com/jeslyztaz/hdb-resale-prices/blob/master/reports/report.md)

## Tools used
1. [Jupyter](https://jupyter.org/)
2. [Pandas](https://pandas.pydata.org/)
3. [SQLAlchemy](https://www.sqlalchemy.org/)
3. [PostgreSQL](https://www.postgresql.org/)
3. [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)

## Project Struture
```
hdb_resale_prices/
│
├── data/                   # Raw and processed data files
│   ├── raw/                # Unprocessed raw data
│   ├── cleaned/            # Processed/cleaned data
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── data cleaning + postgresql.ipynb
│
├── reports/                # Generated visualisations and reports
│   └── code_screenshots/   # Code screenshots used for the report
│   └── dashboard_images/   # Visualisations from Power BI
│   └── dashboard.pbix      # Power BI dashboard file
│   └── report.md           # Project report
│
├── README.md               # Project overview and documentation
├── config.yaml             # File for local database
└── .gitignore              # Files and folders to ignore in Git
```
