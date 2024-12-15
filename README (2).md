# Symmetrical Telegram

```
pip install requirements.txt
```

This is a project on HDB Resale Housing prices in Singapore. The dataset can be found [here](https://data.gov.sg/collections/189/view).
All the code can be found in [notebook](https://github.com/jeslyztaz/symmetrical-telegram/blob/master/notebooks/data%20cleaning%20%2B%20postgresql.ipynb)
For a detailed analysis, please refer to this [writeup](https://github.com/jeslyztaz/symmetrical-telegram/blob/master/)

## Tools used
1. [Jupyter](https://jupyter.org/)
2. [Pandas](https://pandas.pydata.org/)
3. [SQLAlchemy](https://www.sqlalchemy.org/)
3. [PostgreSQL](https://www.postgresql.org/)
3. [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)

## Project Struture
```
resale_housing_prices/
│
├── data/                   # Raw and processed data files
│   ├── raw/                # Unprocessed raw data
│   ├── cleaned/            # Processed/cleaned data
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── data cleaning + postgresql.ipynb
│
├── reports/                # Generated visualisations and reports
│   └── dashboard_images/   # Visualisations from Power BI
│   └── dashboard.pbix      # Power BI dashboard file
│   └── report.md           # Project report
│
├── README.md               # Project overview and documentation
├── config.yaml             # File for local database
├── .gitignore              # Files and folders to ignore in Git
└── main.py                 # Main script to run the entire pipeline
```