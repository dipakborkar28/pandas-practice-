import pandas as pd 
df = pd.read_csv(r"C:\Users\Admin\Downloads\pandas_practice_dataset.csv")

print(pd.isnull(df).sum())
print(pd.notnull(df).sum())
print(df)
print(df.dropna())
print(df.fillna(5))

