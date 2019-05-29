# generate .csv from .xlsx file
import pandas as pd

# read csv
import csv

# import numpy
import numpy as np


def read_from_csv(path, fileName):
    csv_file=open(path+fileName)
    # read .csv from line to line
    csv_reader_lines = csv.reader(csv_file)
    reslist = []
    for one_line in csv_reader_lines:
        reslist.append(one_line)
    return reslist


def matrix_gene(path):
    orderlist = read_from_csv(path, "TableA-Orders.csv")
    check = read_from_csv(path, "TableC-DistanceMatrix.csv")
    city_num=len(check)
    item_num=len(orderlist)
    matrix = np.zeros((city_num+1, city_num+1), dtype=float)
    for counter in range(1,item_num):
        i = int(orderlist[counter][0])
        j = int(orderlist[counter][1])
        matrix[i][j] += 1.0
    return city_num, matrix


if __name__ == '__main__':
    path="../sourceData/"
    fileName = "TableA-Orders.csv"
    city_num, matrix=matrix_gene(path)
    for i in range(city_num):
        for j in range(city_num):
            print(matrix[i][j],end=' ')
        print(" ")