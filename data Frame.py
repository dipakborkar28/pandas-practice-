import pandas as pd

student = {
    "Roll": [1, 2, 3, 4],
    "Name": ["naruto ", "kakashi", "sasuke", "kurama"],
    "Marks": [85, 92, 78, 65]
}

df = pd.DataFrame(student)


# print(df)
print("akasuki\n",df.iloc[2])
# print(df.iloc[0])
# print(df.iloc[1:3])
print(df.loc[2])