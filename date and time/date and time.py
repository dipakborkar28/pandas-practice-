import pandas as pd 
df = pd.DataFrame({
    "name" : ["payal", "dipak","rani","anil"],
    "date" : ["2026-07-23","2026-03-26","2023-01-12","2016-09-09"]

})

df["date"] = pd.to_datetime(df["date"])
#this statement helps to the pandas that is not string is date 
print(df)
print(df["date"].dt.year)
print(df["date"].dt.month)
print(df["date"].dt.day)
#here we use .dt beacuse   it gives us to the access of date related properties 
print(df["date"].dt.day_name())
print(df["date"].dt.month_name())


