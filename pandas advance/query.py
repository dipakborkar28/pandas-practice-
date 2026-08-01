import pandas as pd

df = pd.DataFrame({
    "Name": ["Dipak", "Rani", "Payal", "Anil"],
    "Marks": [90, 80, 70, 95],
    "Department": ["CSE", "IT", "CSE", "IT"]
})

print(df)
#df[df["Marks"] > 80]  insted of using this we use it 

print(df.query("Marks >80"))

print(df.query('Marks > 80 and Department == "IT"'))
# in this statement we use double condition for that we double inverted and single inverted togatherly
    # and for combining the both statement togather and called togatherly 
print(df.query('Department == "CSE" or Marks > 90'))
#Think of query() as writing a simple English sentence.