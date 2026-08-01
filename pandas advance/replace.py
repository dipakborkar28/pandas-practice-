import pandas as pd

df = pd.DataFrame({
    "Name": ["Dipak", "Rani", "Payal", "Anil"],
    "Gender": ["M", "F", "F", "M"],
    "Marks": [90, 80, 70, 60]
})

print(df)
df["Gender" ] = df["Gender"].replace("M","male") 
print(df)

# now with the help of replace statement we can replace the data in column

df["Gender"] = df["Gender"].replace({
    "male" : "men",
    "F" : "women"

})
print(df)
# changing one value and changing multiple values are quite different check closily
# , replace with the : in multiple value

df["Marks"] = df["Marks"].replace(70,89)
print(df)
# this statement change the marks 70 to 89 
# it is different than map beacuse map work on series and it work on dataframe
