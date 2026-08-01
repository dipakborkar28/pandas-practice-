import pandas as pd
student_df =  pd.DataFrame({
    "name" : ["Dipak","Payal","Anil","Rani"],
    "department" : ["CSE","Civil","Civil","CSE"],
    "gender" :  ["Male","Female","Male","Female"],
    "marks" : [67,89,56,99] 
       })  
average_marks = pd.pivot_table(
    student_df,
    values="marks",
    index="department",
    columns="gender",
    aggfunc="mean"
)
print(student_df)
print(average_marks)
#! values are the column which is calculated
#! index are the what should become the rows
#! columns  are the become the column 
#! aggfunc is the calucation should perform 
#? we can also perform the 'sum' 'count' 'min' 'max'
# Rows → index
# Columns → columns
# Data → values
# Calculation → aggfunc


