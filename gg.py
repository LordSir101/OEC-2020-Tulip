import pandas as pd
import numpy as np
Starting = []
Initial = []
df1 = pd.read_csv('gg.csv')
arr = df1.to_numpy()
for x in arr:
    if x[0] ==0:
        Starting.append(x)
    else:
        Initial.append(x)
Energyarr = Starting[1][3:9]
colvals = ["Solar","Nuclear","Wind","Hydro","Gas/oil","Biofuel","Neighboor"]
Dict1 = dict(zip(colvals,Energyarr))
print(Dict1['Solar'])
print(Dict1)
