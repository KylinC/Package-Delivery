###################################################
# This python file refactor .csv file to .npy
# Which is provided to read-in by np
# function_list:
# disMatrix_to_npy(disMatrixFile, npyFile) --return (1)pandasDataFrame
###################################################

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


def disMatrix_to_npy(disMatrixFile, npyFile):
    csv = pd.read_csv(disMatrixFile, encoding='utf-8')
    dataframe = pd.DataFrame(csv.values, index=range(1, csv.index[-1] + 2))
    dataframe = dataframe.T
    dataframe[0] = list(map(float, csv.columns))
    dataframe = dataframe.sort_index(axis=1)
    np.save(npyFile, dataframe.values)
    return dataframe


def OrderMatrix(OrderFile):



def TransportMatrix(TransportFile):



def CargoMatrix(CargoFile):
    


def DataNpyTest():
    print(disMatrix_to_npy("../sourceData/TableC-DistanceMatrix.csv", "../sourceData/TableC-DistanceMatrix.npy"))
    pass


if __name__ == '__main__':
    DataNpyTest()