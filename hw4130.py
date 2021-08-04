import csv
import pandas as pd

data = pd.read_csv("mergeddatanew.csv")
data= data.dropna()
print(data.shape)

deletedata = ["Luminosity", "nolabel", "temp_Star_name", "temp_Mass"]

for i in deletedata:
    del data[i]
print("Data successfully cleaned!")

print(data.shape)
