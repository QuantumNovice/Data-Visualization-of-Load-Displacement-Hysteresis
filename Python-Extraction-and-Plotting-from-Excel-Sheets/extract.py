import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits import mplot3d
from numpy import *


loc = ("Wall No.3_ Data.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(2)

def load_col(start_row, col):
    x = 0
    data  = []
    i = start_row
    while x != '':
        #print(x)
        try:
            x = sheet.cell_value(i, col)
            data.append(x)
            #print(x)
            i += 1
        except IndexError:
            break
    return data

def sanitize(data):
    refined = []
    for i in data:
        if type(i) == float:
            refined.append(i)
        else:
            refined.append(0.0)
    return refined

load = sanitize(load_col(4, 2))
disp = sanitize(load_col(4, 3))
csv = ''
for i in range(len(load)):
    csv += '{},{}\n'.format(load[i], disp[i])
with open('data.csv', 'w') as afile:
    afile.write(csv)


  

