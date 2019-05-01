import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits import mplot3d
from numpy import *
from matplotlib import animation


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


def anim(index):
    fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #plt.subplot(2, 2, index+1)
    ax = plt.axes(xlim=(min(DISP[index] ), max(DISP[index] )),
                  ylim=(min(LOADS[index]), max(LOADS[index])))

    line, = ax.plot([], [],lw=2)
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(DISP[index][:i], LOADS[index][:i])
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                 frames=len(LOADS[index]), interval=0, blit=True)
    
    plt.grid()
    plt.xlabel('Displacement (mm)')
    plt.ylabel('Load (Tons) ')
    anim.save('{}.gif'.format(index), fps=30)
    #plt.show()
    
for i in range(4,18):
    anim(i)

