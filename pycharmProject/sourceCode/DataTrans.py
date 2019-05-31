#######################################################
# This file include data pre-process function
# xlsx_to_csv(source_file, aim_file)
# xlsx_to_csv_pd(source_file, aim_file)
# csv_to_xlsx(source_file, aim_file)
# csv_to_xlsx_pd(source_file, aim_file)
#######################################################

import pandas as pd
import codecs
import numpy as np
import xlrd
import xlwt
import csv


def xlsx_to_csv(source_file, aim_file):
    workbook = xlrd.open_workbook(source_file)
    table = workbook.sheet_by_index(0)
    with codecs.open(aim_file, 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)


def xlsx_to_csv_pd(source_file, aim_file):
    data_xls = pd.read_excel(source_file, index_col=0)
    data_xls.to_csv(aim_file, encoding='utf-8')


def csv_to_xlsx(source_file, aim_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')
        l = 0
        for line in read:
            r = 0
            for i in line:
                sheet.write(l, r, i)
                r = r + 1
            l = l + 1
        workbook.save(aim_file)


def csv_to_xlsx_pd(source_file, aim_file):
    csv = pd.read_csv(source_file, encoding='utf-8')
    csv.to_excel(aim_file, sheet_name='data')


def DataTransTest():
    xlsx_list=["../rawData/TableA-Orders.xlsx", "../rawData/TableB-Commodities.xlsx",
                 "../rawData/TableC-DistanceMatrix.xlsx", "../rawData/TableD-TransportationTools.xlsx"]
    csv_list=["../sourceData/TableA-Orders.csv", "../sourceData/TableB-Commodities.csv",
                 "../sourceData/TableC-DistanceMatrix.csv", "../sourceData/TableD-TransportationTools.csv"]
    xlsx_out_list=["../sourceData/TableA-Orders.xlsx", "../sourceData/TableB-Commodities.xlsx",
                 "../sourceData/TableC-DistanceMatrix.xlsx", "../sourceData/TableD-TransportationTools.xlsx"]
    for i in range(4):
        xlsx_to_csv(xlsx_list[i],csv_list[i])
        pass
    csv_to_xlsx(csv_list[1],xlsx_out_list[1])
    pass

if __name__ == '__main__':
    DataTransTest()