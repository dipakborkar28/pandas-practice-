import pandas as pd 
df = pd.DataFrame({
    "name" : ["dipak","rani","payal","anil"],
    "marks": [90,89,28,65]
})
df["marks"] = df["marks"].apply(lambda x:  x+5)

#it adds 5 marks to every students marks 
#lambda x: x + 5 it means "Take each value (x) and return x + 5."

df["result"]= df["marks"].apply(lambda x: "pass"  if x > 35 else "fail" )
# this is use as a condition of if else show s the 
#above where we print the passing studetns
df["name"] = df["name"].apply(lambda x: x.upper())
print(df)