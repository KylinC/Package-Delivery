import pandas as pd
import csv
import numpy as np
import sys

from DataMatri import *

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem4/sol_cost"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

cargolist = cargoMatrix("../sourceData/TableB-Commodities.csv")
cargolist = cargolist.values

cost = 0
csv = pd.read_csv("/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem4/orders.csv", encoding='utf-8')
dataframe = pd.DataFrame(csv)
for idx, column in dataframe.iterrows():
    typed = int(column["Commodity Index"])-1
    cost += float(lines1[idx]) * int(column["Amount of Commodity"]) * float(cargolist[typed][3])
    pass

print(cost)