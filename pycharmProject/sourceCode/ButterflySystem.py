##################################################
# Do not go gentle into that good night
#
# Butterfly System provide a reverse random-attractant model to online-update random distribution!
# The function prototypes are as follows:
#     - NonePheromone
#     - Pheromone
##################################################

# batch method
from gurobipy import *

# data pre-process
import pandas as pd
import csv
import numpy as np

# visualization package
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go

import scipy.special
# the sigmoid function-
# method: expit()

class ButterflySystem:
    # init the variables of butterfly
    def __init__(self, CSVFilePath, NodeNumber, ContainerList=[250,600,1000,2000]):
        self.filePath = CSVFilePath
        self.nodeNumber = NodeNumber
        self.containerList = ContainerList

    # feed the system

    @staticmethod
    def OrdersPack():
