import pandas as pd 
students  = pd.DataFrame({
    "Roll" : [1,2,3],
    "name" : ["rani","dipak","anil"]


})
name = pd.DataFrame({
    "Roll" : [2,3,4],
    "marks": [56,78,98]
})
# !inner merge (most common )
A = pd.merge(students,name, on="Roll", how="inner")
print(A)
# here the we merge function and innerformat 
# it give the common element in both the dataframe 
#in this case it give s the 2,3

#! left join
B = pd.merge(students,name, on= "Roll", how="left")
print(B)
# just like the name it give s the all element in left  meaning students and 
#common element in the right meaning in name so it output contain 
#1,2,3, not 4 beacuse it is not in left and not  in common

#! right join
C = pd.merge(students,name,on="Roll",how="right")
print(C)
# this work same as the left join but on the right side thats it

#!out join
D = pd.merge(students,name,on="Roll",how="outer")
print(D)