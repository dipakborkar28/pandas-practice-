import pandas as pd 
df = pd.DataFrame({
    "name" : ["payal", "dipak","rani","anil"],
    "date" : ["2026-07-23","2026-03-26","2023-01-12","2016-09-09"]

})
df["date"] = pd.to_datetime(df["date"])
print(df[df["date"] > "2025-07-23"])
print(df[df["date"] < "2025-07-23"])
print(df[df["date"] == "2026-07-23"])