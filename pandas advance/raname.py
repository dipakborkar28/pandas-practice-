import pandas as pd

df = pd.DataFrame({
    "Roll": [101, 102, 103],
    "Name": ["Dipak", "Rani", "Payal"],
    "Marks": [90, 80, 70]
})

print(df)
df = df.rename(columns={"Marks" : "score",
                        "Name"   : "Ids"
})
# rename is help to rename any colunm and we can rename multiple columns at once 
print(df)
# we can also rename the index 
df = df.rename(index={
    0 : "a",
    1 : "b",
    2 : "C"
})
print(df)
# it do not change the original dataframe to change the original dataframe use inplace= true
