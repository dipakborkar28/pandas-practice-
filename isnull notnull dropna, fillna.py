import pandas as pd 
df = pd.read_csv("dipak.csv")

print(pd.isnull(df).sum())
#This returns True for missing values and False for non-missing values.
print(pd.notnull(df).sum())
#It checks whether values are not missing.
print(df)
print(df.dropna())
# it remove s all none values 

print(df.fillna(5))
#it fills the misssing  values 

