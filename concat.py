import pandas as pd

df1 = pd.DataFrame({
    "Roll":[1,2],
    "Name":["Amit","Neha"]
})

df2 = pd.DataFrame({
    "Roll":[3,4],
    "Name":["Ravi","Priya"]
})

print(pd.concat([df1,df2],ignore_index=True))
#concat just put the one dataframe below the other
#?gnore work to correct the indexing and put them in correct order
#! we write it in the list beacuse it expect only the list 

df3 = pd.DataFrame({
    "name": ["dipak","rani","payal","anil"]
})
df4 = pd.DataFrame({
    "roll": [89,78,56,45]
})
print(pd.concat([df3,df4], axis=1))
#here we have the two dataframe each having only pone series 
#with the help concat we merrge them
#!axis 1 help the position of each series to correct in position 
print("learning git is fun ")
