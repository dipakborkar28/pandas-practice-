import pandas as pd

students = pd.DataFrame({
    "Roll": [1, 2, 3, 4],
    "Name": ["Amit", "Neha", "Ravi", "Priya"]
})

marks = pd.DataFrame({
    "Roll": [1, 2, 3, 4],
    "Marks": [85, 92, 78, 65]
})
print(pd.merge(students,marks,on="Roll"))