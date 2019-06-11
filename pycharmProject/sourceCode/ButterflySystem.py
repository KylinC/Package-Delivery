###################################################################################################################
# Butterfly System provide a reverse random-attractant model to online-update random distribution!
# `Class ButterflyNet provide a link-list relation in order to shorten running time
# `Class ButterflyNet provide a time-slice method to solver SFRouting
#     - init: read the data: order.csv  truck.csv  ship.csv  train.csv  plane.csv  as pandas.dataframe
#              (prototype: Butterfly.df)
#       - parse_matrix: slice the 24 hours into batch-slice and muti-process every time-slice to
#               generate init transport-matrix
#
#        Butterfly will achieve a random-method to find the approximation solution using Google's page algorithm
#        KylinChen, www.kylinchen.top, k1017856853@icloud.com
###################################################################################################################

# batch method
# from gurobipy import *

# data pre-process
import pandas as pd
import csv
import numpy as np
import sys

# visualization package
import matplotlib.pyplot as plt
# import plotly
# import plotly.graph_objs as go

# the sigmoid function-
# method: expit()
# import scipy.special

# achieve muti-process
import multiprocessing as mp
# import threading as td
import time


# Data class
class ButterflyNet:
    # init the variables of butterfly_net
    def __init__(self, NodeNumber, BatchNumber):
        self.nodeNumber = NodeNumber
        self.batchNumber = BatchNumber
        self.network = []
        for idx in range(BatchNumber):
            self.network.append([])
            for idy in range(NodeNumber+1):
                self.network[idx].append([])

    def networkOut(self):
        print(len(self.network))
        print(len(self.network[0]))
        # print(len(self.network[23]))

    def addTag(self, tag):
        self.network.append(tag)

    def addItem(self, source, sink, offset, cost):
        self.network[0][source].append((sink, offset, cost))

    def Index(self, location):
        return self.network[location]


# Method class
class ButterflySystem:
    # init the variables of butterfly_system
    def __init__(self, CSVFilePath, NodeNumber, BatchNumber=24):
        self.filePath = CSVFilePath
        self.nodeNumber = NodeNumber
        self.batchNumber = BatchNumber
        self.hushkeys = self.keys_generator(NodeNumber**1.4)
        self.orders_df = self.read_orders()
        self.trans_df_list = self.read_trans()
        self.slice_dict = {}

    def parse_matrix(self):
        manager = mp.Manager()
        queue = manager.Queue()
        processpool = []
        time_slice = 24*60//self.batchNumber
        for idx in range(self.batchNumber):
            start = idx*time_slice
            end = (1+idx)*time_slice
            processpool.append(mp.Process(target=self._parse_matrix_subprocess, args=(idx, start, end, queue, )))
            processpool[idx].start()
        for idx in range(self.batchNumber):
            processpool[idx].join()
        for idx in range(self.batchNumber):
            mat = queue.get()
            self.slice_dict[mat.Index(1)] = mat.Index(0)
            pass
        pass

    def _parse_matrix_subprocess(self, tag, start, end, queue):
        res = ButterflyNet(self.nodeNumber, 1)
        res.addTag(tag)
        for transport in range(4):
            # [0]:truck, [1]:train, [2]:ship, [3]:plane
            dataframe = self.trans_df_list[transport]
            aim_df = dataframe.loc[(dataframe["Departure time"] >= start) & (dataframe["Departure time"] < end)]
            for idx, column in aim_df.iterrows():
                source = int(column["Departure city index"])
                sink = int(column["Arrival city index"])
                offset = column["Arrival time"]//(end - start)
                cost = column["Cost for every 1kg good"]
                res.addItem(source, sink, offset+1, cost)
                print(tag, idx)
        queue.put(res)
        # sys.exit()

    def data_out(self):
        return self.slice_dict

    def read_orders(self, rewrite=0):
        csv = pd.read_csv(self.filePath + "/orders.csv")
        dataframe = pd.DataFrame(csv)
        dataframe = dataframe.sort_values(by=["City of Seller", "City of Purchaser", "Time of Order"])
        # change by items in list of dataframe.columns
        if (rewrite):
            dataframe.to_csv(self.filePath + "/orders.csv", encoding='utf-8')
            pass
        # dataframe.to_csv("../sourceData/orders.csv")
        return dataframe
        pass

    def read_trans(self, rewrite=0):
        transport = ["/truck.csv", "/train.csv", "/ship.csv", "/plane.csv"]
        DFlist = []
        for file in transport:
            csv = pd.read_csv(self.filePath + file)
            dataframe = pd.DataFrame(csv)
            dataframe = dataframe.sort_values(by=["Departure time",  "Arrival time"])
            if (rewrite):
                dataframe.to_csv(self.filePath + file, encoding='utf-8')
                pass
            DFlist.append(dataframe)
        return DFlist
        pass

    # feed the system
    # @staticmethod
    def keys_generator(self, num):
        keylist=[]
        for idx in self.prime_generator():
            if idx < num:
                keylist.append(idx)
                pass
            else:
                break
        return keylist
        pass

    # @staticmethod
    def odd_generator(self):
        idx = 1
        while True:
            idx += 2
            yield idx

    def not_divisible(self, n):
        return lambda x: x % n > 0

    def prime_generator(self):
        idx = 2
        it = self.odd_generator()
        while True:
            idx = next(it)
            yield idx
            it = filter(self.not_divisible(idx), it)

    def KeyOut(self):
        print(self.hushkeys)

if __name__ == '__main__':
    # m=ButterflySystem("../sourceData/change", 665, 24)
    # m.KeyOut()
    # k=ButterflyNet(645, 1)
    # k.networkOut()
    st1 = time.time()
    m = ButterflySystem("../sourceData/change", 656, 24)
    m.parse_matrix()
    st2 = time.time()
    print("time: ", st2-st1)
    print(m.slice_dict[1])
