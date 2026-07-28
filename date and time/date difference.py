import pandas as pd 
df = pd.DataFrame({
    "name" : ["dipak","payal","rani"],
    "joining_date" : ["2026-07-23","2026-03-26","2023-01-12"]
    
})
df["joining_date"] = pd.to_datetime(df["joining_date"])
today = pd.Timestamp("2026-07-27")
df["days since joining"] = today - df["joining_date"]
print(df)
# it gives us the difference between the our joining date and todays date 
df["Days Since Joining"] = (
    today - df["joining_date"]
).dt.days
print(df)
# this give only number of days 
