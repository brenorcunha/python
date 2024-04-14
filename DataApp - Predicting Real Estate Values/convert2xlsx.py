import pandas as pd

# Leia o arquivo .csv
df = pd.read_csv('housing.csv')

# Salve o DataFrame como .xlsx
df.to_excel('housing.xlsx', index=False)
