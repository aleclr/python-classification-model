import pandas as pd

url = 'C:\BD6_Noite_413c\Lab6\python-classification-model\employee.csv'

data = pd.read_csv(url)

print(data.head(5))

data.info()

print(data.duplicated().sum())
# print(data.dtypes)
# print(data.isnull().sum())

# TRATAMENTO DE DADOS
# identificar e mostrar os registros duplicados
print('TRATAMENTO DE DADOS')
d = data[data.duplicated(keep = False)]
print(d.sort_values(by = list(data.columns)).head(20))

# dataset shape
print(data.shape)

# identificar registros nulos
print(data.isna().sum())