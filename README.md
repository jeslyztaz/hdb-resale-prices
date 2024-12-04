# This is a project on HDB resale housing prices

```
resale_housing_prices/
│
├── data/                   # Raw and processed data files
│   ├── raw/                # Unprocessed raw data
│   ├── cleaned/            # Processed/cleaned data
│
├── database/               # Database schema and SQL scripts
│   ├── schema.sql          # PostgreSQL schema definition
│   ├── init.sql            # Initialization scripts
│
├── src/                    # Source code
│   ├── data_cleaning.py    # Data cleaning and validation scripts
│   ├── database.py         # Scripts to interact with the database
│   ├── visualizations.py   # Scripts for generating visualizations
│   ├── config.py           # Configuration variables (e.g., database credentials)
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── data_analysis.ipynb
│   ├── visualization.ipynb
│
├── tests/                  # Unit and integration tests
│   ├── test_data_cleaning.py
│   ├── test_database.py
│
├── logs/                   # Logs for debugging
│   ├── app.log
│
├── reports/                # Generated visualizations and reports
│   ├── dashboard.pbix      # Power BI dashboard file
│
├── requirements.txt        # Python dependencies
├── README.md               # Project overview and documentation
├── .gitignore              # Files and folders to ignore in Git
└── main.py                 # Main script to run the entire pipeline
```


### Project Objectives/Framework
- Jupyter Notebook for EDA
#### Python
- Data cleaning (pandas)
- Data validation (jsonschema)
- ORM for interactions between Python and PostgreSQL (sqalchemy)
#### PostgreSQL 
Data storage to store cleaned data
#### PowerBI
- Visualisations
- Connect Power BI using native PostgreSQL connector
