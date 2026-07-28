import pandas as pd 
#!Many real datasets contain text like names, emails, cities, and 
# !phone numbers. Pandas provides the .str accessor to work with text columns.
df = pd.DataFrame({
    "name" : ["dipak", "Rani", "payal", "ANIL"]

})
A= df["name"].str.upper()
D = df["name"].str.lower()
w = df["name"].str.len()
f = df["name"].str.contains("a",case=False)
#contains is a case sensitive that why we use case = false
print(A)
print(D)
print(f)
print(w)