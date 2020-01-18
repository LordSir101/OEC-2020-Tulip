import pandas as pd
import numpy as np
Starting = []
Initial = []
df1 = pd.read_csv('gg.csv',names=["Index","Time","Solar","Nuclear","Wind","Hydro","Gas/oil","Biofuel","Neighboor",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
arr = df1.to_numpy()
for x in arr:
    if x[0] ==0:
        Starting.append(x)
    else:
        Initial.append(x)
Energyarr = Starting[0][3:9]
colvals = ["Solar", "Nuclear", "Wind", "Hydro", "Gas/oil", "Biofuel", "Neighboor"]
Dict1 = dict(zip(colvals , Energyarr))
print(Dict1)

