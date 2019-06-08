##################################################
# This .py file contains some function with API(choose necessary parameters) to solve corresponding problem
# The function BSearch() contains parameters as follow:
# - commonDeltaT: which means the interval time between order established and orders sent(common orders)
# - specialDeltaT: which means the interval time between order established and orders sent(special orders)
# - commonDDL: which means the DDL of arrival destination(common orders)
# - specialDDL: which means the DDL of arrival destination(special orders)
# KylinC, 6,5, 2019
##################################################

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

# Import DataFrame-read-in module
from DataMatri import *


# problem 1 function
def dfSearch(commonDeltaT, specialDeltaT, commonDDL, specialDDL, containerList=[1000, 1000, 1000, 1000]):
    C_DF=disMatrix_to_npy("../sourceData/TableC-DistanceMatrix.csv", "../sourceData/TableC-DistanceMatrix.npy")
    # A_DF=orderMatrix("../sourceData/TableA-Orders.csv")
    A_DF = orderMatrixD("../sourceData/change/orders.csv")
    ############################
    print(A_DF)
    ############################
    transport_list = ["../sourceData/TableD-Plane.csv", "../sourceData/TableD-Ship.csv",
                      "../sourceData/TableD-Train.csv", "../sourceData/TableD-Truck.csv"]
    change_transport_list=["../sourceData/change/plane.csv", "../sourceData/change/ship.csv",
                      "../sourceData/change/train.csv", "../sourceData/change/truck.csv"]
    # D_DFList=transportMatrix(transport_list)
    D_DFList=transportMatrix(change_transport_list)
    B_DF=cargoMatrix("../sourceData/TableB-Commodities.csv")
    # index of all the orders
    order_column=A_DF.columns
    transport_column=D_DFList[0].columns
    # Set a dic to check the transport is full or not
    containerCheck=[{}, {}, {}, {}]
    ResDF=A_DF
    order_index = ResDF.index
    transport_name=["Plane", "Ship", "Train", "Truck"]
    # print(order_index)
    # print(order_column)
    for idx, order_item in A_DF.iterrows():
        # index format (A_DF.loc[order_item, "City of Seller"])
        source = order_item[order_column[0]]
        order_time = order_item[order_column[-1]]
        sink = order_item[order_column[1]]
        order_number = order_item[order_column[-3]]
        emergency_tag = order_item[order_column[-2]]

        # Build a search index to make the search sequence OPT
        searchQ = [3, 2, 1, 0]
        deltaTime=commonDeltaT
        DDL=commonDDL
        if(emergency_tag):
            searchQ.reverse()
            deltaTime=specialDeltaT
            DDL=specialDDL
        OPT_transport=-1
        OPT_transport_number=-1
        OPT_cost_per=10000

        # search OPT transport method
        for transport in searchQ:
            # print(transport)
            feasible_field = D_DFList[transport].loc[lambda df: D_DFList[transport][transport_column[0]] == source]
            # print(feasible_field.index)
            feasible_field = feasible_field.loc[lambda df: feasible_field[transport_column[1]] == sink]
            # if not have any search results
            if (len(feasible_field)==0):
                # print("back")
                continue

            # sort by departure time
            feasible_field=feasible_field.sort_values(by=[transport_column[-1]])
            # match the feasible one
            OPT_index=feasible_field.index
            for idx2, transport_number in feasible_field.iterrows():
                # check departure time
                transport_time = transport_number[transport_column[-1]]
                transport_DDL = transport_number[transport_column[2]] + transport_time
                transport_cost_per = transport_number[transport_column[-2]]

                # once i not satisfied, all j>i not satisfied because dataframe.sort
                if(transport_time > order_time + deltaTime):
                    break

                # Check Route full
                if(idx2 in containerCheck[transport]):
                    if(order_number > containerCheck[transport][idx2]):
                        continue
                    else:
                        containerCheck[transport][idx2] -= order_number
                else:
                    containerCheck[transport][idx2]=containerList[transport]-order_number

                # check price OPT more
                if(transport_DDL <= DDL and transport_cost_per < OPT_cost_per):
                    OPT_transport = transport
                    OPT_transport_number = idx2
                    OPT_cost_per = transport_cost_per

        #if (OPT_transport==-1 and OPT_transport_number==-1):
            #raise UDError(0)
        print("%d th, from %d to %d, takes %s, number %d " %(idx,source,sink,transport_name[OPT_transport],OPT_transport_number))
        ResDF.loc[order_index[idx], "Transport"] = transport_name[OPT_transport]
        ResDF.loc[order_index[idx], "Vehicle"] = OPT_transport_number
        # print("success")
        pass

    ResDF.to_csv("../outData/out.csv")


class UDError(Exception):
    print("search error")
    pass

if __name__ == '__main__':
    dfSearch(120, 60, 3600, 1800, [50, 100, 150, 200])