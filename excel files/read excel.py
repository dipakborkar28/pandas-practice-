import pandas as pd 
df = pd.read_excel(r"C:\Users\Admin\Downloads\Pandas_Practice_Students.xlsx")
# here we use r to for using file path 
print(df)
df.to_excel("rani.xlsx", index=False)
# to excel creates an Excel file that you can open in Microsoft Excel.
# also with this function we can dataframe in excel file
# index = fasle to avoid the index
