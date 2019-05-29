# import pandas to transfer .xlsx to .csv
import pandas as pd

def xlsx_to_csv_pd(path,fileName):
    data_xls = pd.read_excel(path+fileName, index_col=0)
    data_xls.to_csv('../csvData/'+fileName[:-4]+"csv", encoding='utf-8')

if __name__ == '__main__':
    path=input("RelativePath: ")
    fileName=input("FileName: ")
    xlsx_to_csv_pd(path,fileName)
