import pandas as pd 
department = {
    "name": ["arjun","dipak","aman","ram","payal","anil","rani"],
    "dep" : ["mech","cse","mech","extc","cse","civil","chem"],
    "marks":[62,22,67,88,46,78,1]
    
}
df = pd.DataFrame(department)
# print("max\n",df.groupby("dep") ["marks"].max())
# print("mean\n",df.groupby("dep") ["marks"].mean())
# print("min\n",df.groupby("dep") ["marks"].min())
# print("sum\n",df.groupby("dep") ["marks"].sum())
# print("count\n",df.groupby("dep") ["marks"].count())
#group by function create the group of same name values 
#df.groupby() only create the group and the operations such as max and mean are 
#use as follow s to calclate sudden group in dataframe
print(df.groupby("dep")["marks"].agg(["mean","max","sum"]))