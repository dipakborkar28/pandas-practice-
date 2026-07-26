import pandas as pd

student = {
    "Roll": [1, 2, 3, 4, 5, 6, 7, 8, ],
    "Name": ["Amit", "Neha", "Ravi", "Priya", "Karan","ram ","sita","payal"],
    "Marks": [85, 92, 78, 65, 88, 586, 56,45]
    
}

df = pd.DataFrame(student)
df.head()
df.head(2)
tail = df.tail()
tail2 = df.tail(3)
shape= df.shape
colume= df.columns
info = df.info()
decribe = df.describe()
print("result\n",shape)