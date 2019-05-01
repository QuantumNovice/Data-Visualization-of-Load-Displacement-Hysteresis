import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits import mplot3d
from numpy import *
import numpy
from mpl_toolkits.mplot3d import Axes3D


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

def running_mean(x, N):
    cumsum = numpy.cumsum(numpy.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

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
    load = array(sanitize(load_col(4,i)))
    disp = array(sanitize(load_col(4, i+1)))
    t = range(len(load))
    
    LOADS.append(load)
    DISP.append(disp)
    T.append(t)
    
  
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax = plt.axes()
#ax.plot3D(load, displacement, t)
#ax.plot3D(load1, displacement1, t1)

#ax = fig.add_subplot(2,2,4, projection='3d')
for i in range(len(LOADS)):
    #print(i)
    #ax.plot3D(LOADS[i], DISP[i], T[i])
    N = 5
    ax.get_proj = lambda: numpy.dot(Axes3D.get_proj(ax), numpy.diag([0.5, 0.5, 3, 1]))
    ax.plot3D( running_mean(LOADS[i], N), running_mean(DISP[i], N), running_mean(T[i], N))
    ax.set_xlabel('Load')   
    ax.set_ylabel('Displacement')
    ax.set_zlabel('Time')
#ax.view_init(100, 100)

#plt.savefig('AVG.png')
plt.show()

