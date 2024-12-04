import pandas as pd

def test():
    file = "data/housing_prices.csv"

    data = pd.read_csv(file, encoding = 'utf-8', errors = 'ignore')
    print(data)

if __name__ == "__main__":
    test()