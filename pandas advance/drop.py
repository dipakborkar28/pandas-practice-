import pandas as pd
df = pd.DataFrame({
    "Roll" : [1,2,3,4],
    "Name" : ["Dipak","Payal","Rani","Anil"],
    "Marks" : [90,89,7,6]
})
df = df.set_index("Roll")
# using set_index you change defaut index

print(df.drop(1))
# drop statement drop the any value in this case it drop s the one numbers value

print(df)
print(df.drop("Marks",axis=1,inplace=True))
#inplace modify  the original dataframe 
#axis = 1 remove the column and axis= 0 remove the rows