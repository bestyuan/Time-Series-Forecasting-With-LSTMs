import xlrd
import numpy as np

a = np.arange(33,45).tolist()
head = [2,3]+a+[52,53]


def read_xlrd(filepath,workname):
    workbook = xlrd.open_workbook(filepath)
    booksheet = workbook.sheet_by_name(workname)
    list=[]
    for row in range(1,booksheet.nrows):
        data = []
        for col in head:
            cel = booksheet.cell(row,col)
            val = cel.value
            if val == '':
                val = float(0)
            # if type(val) == str:
            #     val = float(int(val))
            val = float(int(val))
            data.append(val)
        list.append(data)
    return list




