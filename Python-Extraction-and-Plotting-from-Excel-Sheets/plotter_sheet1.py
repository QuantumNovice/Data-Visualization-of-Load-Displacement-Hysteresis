import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits import mplot3d
from numpy import *

loc = ("Wall No.3_ Data.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

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

##load = sanitize(load_col(4,2))
##displacement = sanitize(load_col(4, 3))
##t = range(len(load))
##
##load1 = sanitize(load_col(4, 4))
##displacement1 = sanitize(load_col(4, 5))
##t1 = range(len(load1))

# 17
LOADS = []
DISP = []
T = []
for i in range(2, 35, 2):
    #print(i, i+1)
    load = array(sanitize(load_col(6, i)))
    disp = array(sanitize(load_col(6, i+1)))
    t = range(len(load))
    
    LOADS.append(load)
    DISP.append(disp)
    T.append(t)
    
  
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax = plt.axes()
#ax.plot3D(load, displacement, t)
#ax.plot3D(load1, displacement1, t1)

ax = fig.add_subplot(2,2,4, projection='3d')
for i in range(len(LOADS)):
    #print(i)
    #ax.plot3D(LOADS[i], DISP[i], T[i])
    plt.subplot(221)
    plt.plot(DISP[i], LOADS[i])
    plt.xlabel('Displacement')
    plt.ylabel('Load')

    plt.subplot(222)
    plt.plot(T[i], DISP[i])
    plt.ylabel('Displacement')
    plt.xlabel('Time')

    plt.subplot(223)
    plt.plot(T[i], LOADS[i])
    plt.ylabel('Load')
    plt.xlabel('Time')

    
    ax.plot3D(LOADS[i], DISP[i], T[i])
    ax.set_xlabel('Load')   
    ax.set_ylabel('Displacement')
    ax.set_zlabel('Time')

#ax.view_init(100, 100)
plt.savefig('CH1.png')
plt.show()

