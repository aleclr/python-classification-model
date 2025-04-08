import pandas as pd

DTYPES = {'diagnosis': str}

url = 'https://raw.githubusercontent.com/goodboychan/goodboychan.github.io/master/_notebooks/dataset/wbc.csv'

wbc = pd.read_csv(url, sep = ',', dtype = DTYPES)

wbc.head(5)

# print(wbc.describe())

print(wbc.head(5))
