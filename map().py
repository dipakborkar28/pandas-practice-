import pandas as   pd
grade = pd.Series(["a","b","c","a"])
grade = grade.map({
    "a" : "dipak",
    "b" : "rani",
    "c" : "payal"
})
print(grade)
