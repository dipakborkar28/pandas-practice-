
import pandas as pd

age = pd.Series(
    [18, 22, 19, 25, 20],
    index=["Amit", "Neha", "Ravi", "Priya", "Karan"]

) 


print(age)
print("age of ravi", age["Ravi"])
print("minimum age ",age.min())
print("maximum age", age.max())
print("avarage age", age.mean())
print ("ages greater than 20 :",age[age > 20])
print("age sum",age.sum())