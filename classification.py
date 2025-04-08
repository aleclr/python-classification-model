import pandas as pd

url = 'C:\BD6_Noite_413c\Lab6\estudos\employee.csv'

data = pd.read_csv(url)

print(data.head(5))

data.info()

print(data.duplicated().sum())
# print(data.dtypes)
# print(data.isnull().sum())

# d = data[data.duplicated(keep = False)]