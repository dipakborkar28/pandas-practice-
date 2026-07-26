import pandas as pd 
department = {
    "name": ["arjun","dipak","aman","ram","payal","anil","rani"],
    "dep" : ["mech","cse","mech","extc","cse","civil","chem"]
    
}
cd = pd.DataFrame(department)
print(cd)
print(cd["dep"].value_counts())