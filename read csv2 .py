import pandas as pd
dipak = pd.read_csv("dipak.csv")
dipak = dipak.set_index("Name")
# print(dipak)
# print(dipak.tail(2))
# print(dipak.max())
# print(dipak.index)
# print(dipak.loc["Pooja"])
print(dipak.loc["payal"])