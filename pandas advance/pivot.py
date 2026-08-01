import pandas as pd 
df = pd.DataFrame({
    "name" : ["Dipak","Dipak","Payal","Payal"],
    "subject" : ["Math","Science","Math","Science"],
    "marks" : [90,85,90,85]
})
student = df.pivot_table(
    index="name",
    columns="subject",
    values="marks"
)
print(student)
cla = df.pivot(
    index="name",
    columns="subject",
    values="marks"
)
print(cla)
# simple and straight forward pivot() not allow duplicate 
# and pivot table allow the duplicat beacuse it allows mean , max, count
# Function	Purpose
# pivot()	Reshape data (no duplicate combinations)
# pivot_table()	Summarize data and handle duplicates
