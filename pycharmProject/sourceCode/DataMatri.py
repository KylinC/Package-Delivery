###################################################
# This python file refactor .csv file to .npy
# Which is provided to read-in by np
# function_list:
# disMatrix_to_npy(string disMatrixFile, string npyFile) --return (1)pandasDataFrame
# OrderMatrix(string OrderFile, int rewrite=0) --return (1)pandasDataFrame
#     rewrite suggests whether to rewrite .csv
# TransportMatrix(string-List TransportFilePile, int rewrite=0) --return (1)pandasDataFrame-list
#     rewrite suggests whether to rewrite .csv
# CargoMatrix(string CargoFile, int rewrite=0) --return (1)pandasDataFrame
#     rewrite suggests whether to rewrite .csv
# kylinC, 5,28,2019
###################################################

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


# table C contains
def disMatrix_to_npy(disMatrixFile, npyFile):
    csv = pd.read_csv(disMatrixFile, encoding='utf-8')
    dataframe = pd.DataFrame(csv.values, index=range(1, csv.index[-1] + 2))
    dataframe = dataframe.T
    dataframe[0] = list(map(float, csv.columns))
    dataframe = dataframe.sort_index(axis=1)
    np.save(npyFile, dataframe.values)
    return dataframe
    pass


# table A contains
def orderMatrix(orderFile, rewrite=0):
    csv = pd.read_csv(orderFile)
    dataframe = pd.DataFrame(csv)
    dataframe = dataframe.sort_values(by=["City of Seller", "City of Purchaser", "Time of Order"])
    # change by items in list of dataframe.columns
    if(rewrite):
        dataframe.to_csv(orderFile, encoding='utf-8')
        pass
    # dataframe.to_csv("../sourceData/orders.csv")
    return dataframe
    pass


def orderMatrixD(orderFile, rewrite=0):
    csv = pd.read_csv(orderFile)
    dataframe = pd.DataFrame(csv)
    dataframe = dataframe.sort_values(by=["City of Seller", "City of Purchaser", "Time of Order"])
    # change by items in list of dataframe.columns
    if(rewrite):
        dataframe.to_csv(orderFile, encoding='utf-8')
        pass
    # dataframe.to_csv("../sourceData/orders.csv")
    return dataframe
    pass


# table D contains
def transportMatrix(transportFilePile, rewrite=0):
    DFlist=[]
    for file in transportFilePile:
        csv = pd.read_csv(file)
        dataframe = pd.DataFrame(csv)
        dataframe = dataframe.sort_values(
            by=["Departure city index", "Arrival city index", "Departure time", "Cost for 50km for every 1kg good "])
        if (rewrite):
            dataframe.to_csv(file, encoding='utf-8')
            pass
        DFlist.append(dataframe)
    return DFlist
    pass


# table B contains
def cargoMatrix(cargoFile, rewrite=0):
    csv = pd.read_csv(cargoFile)
    # correct the corresponding index
    dataframe = pd.DataFrame(csv.values, index=range(1, csv.index[-1] + 2), columns=csv.columns)
    if (rewrite):
        dataframe.to_csv(cargoFile, encoding='utf-8')
        pass
    return dataframe
    pass


# test function 1
def DataNpyTest():
    transport_list=["../sourceData/TableD-Plane.csv", "../sourceData/TableD-Ship.csv",
                    "../sourceData/TableD-Train.csv", "../sourceData/TableD-Truck.csv"]
    # print(disMatrix_to_npy("../sourceData/TableC-DistanceMatrix.csv", "../sourceData/TableC-DistanceMatrix.npy"))
    # print(orderMatrix("../sourceData/TableA-Orders.csv"))
    # print(transportMatrix(transport_list))
    test = cargoMatrix("../sourceData/TableB-Commodities.csv")
    print(test.values)
    pass


if __name__ == '__main__':
    DataNpyTest()