##################################################
# This .py file provide a hour-devide-conquer method to call gorubi to get the opt-answer
# KylinC, 6,9, 2019
# pandasDataInit(timeInterval, orderDataframe, nodeNumber): return orders matrix in timeInterval(two-item list)
# !! attention, timInterval's time span must be devisible by 24*60
##################################################

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import gurobipy

# Import DataFrame-read-in module
from DataMatri import *


def pandasDataInit(timeInterval, orderDataframe, commoditiesDataframe, nodeNumber):

    # A list to contain order matrix
    deltaTime = timeInterval[1] - timeInterval[0]
    loopNum = int(24*60 /deltaTime)

    # sort the order dataframe by arrival time to shorten the write-in time
    timeDataframe = orderDataframe.sort_values(by=["Time of Order", "City of Seller", "City of Purchaser"])
    # City of Seller, City of Purchaser, Time of Order origin, Commodity Index, Amount of Commodity,
    # Whether Emergency? (Yes:1 No:0),
    # Time of Order
    dataframeColumn = orderDataframe.columns
    # provide the weight per unit
    commoditiesMatrix = commoditiesDataframe.values

    # contain devide order-matrix
    orderMatrix = np.zeros((loopNum+1, nodeNumber+1, nodeNumber+1))

    for idx, order_item in orderDataframe.iterrows():
        offset = int(order_item[dataframeColumn[-1]]/deltaTime + 1)
        source = int(order_item[dataframeColumn[0]])
        sink = int(order_item[dataframeColumn[1]])
        commoditiesIndex = order_item[dataframeColumn[3]]
        orderMatrix[offset][source][sink] += order_item[dataframeColumn[4]] * commoditiesMatrix[commoditiesIndex-1][3]
        print(idx,)
    return orderMatrix




def mygurobi():
    pass


def PSTest():
    # read data frame as parameter of datainit function
    orderdataframe = orderMatrixD("../sourceData/change/orders.csv")
    commoditydataframe = cargoMatrix("../sourceData/TableB-Commodities.csv")
    nodeNumber = 656
    timelist=[0, 60]
    matrix = pandasDataInit(timelist, orderdataframe, commoditydataframe, nodeNumber)
    for i in range(25):
        for j in range(nodeNumber+1):
            for k in range(nodeNumber+1):
                print(matrix[i][j][k], end=' ')
            print('\n')
        print("+++++++++++++++++++++++++++++++++++")


class DataInitError(Exception):
    print("data error")
    pass


class CallError(Exception):
    print("call error")
    pass


if __name__ == '__main__':
    PSTest()