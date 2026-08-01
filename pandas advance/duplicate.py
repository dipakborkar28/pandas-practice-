import pandas as pd

df = pd.DataFrame({
    "Roll": [101, 102, 103, 103],
    "Name": ["Dipak", "Rani", "Payal", "Payal"],
    "Marks": [90, 80, 70, 70]
})

print(df)
print(df.duplicated())
# the is return the true or false value and this tell us which are the duplicate rows 


print(df.drop_duplicates())
# it eleminate the duplicate rows 

#! keep
print(df.drop_duplicates(keep= "last"))




