import csv

load = []
disp = []

def setup():
    global load, disp
    size(700, 600)
    with open("E:\Coding\Data Visualizatin Techique\data.csv") as afile:
        csv_reader = csv.reader(afile)
        for row in csv_reader:
            load.append(float(row[0]))
            disp.append(float(row[1]))
            #print(float(row[0]), float(row[1]))
            
    
    
i = 0
m = 0
data_x = []
data_y = []
def draw():
    global load, disp, i, m, data_x, data_y
    background(255)
    translate(width/2, height/2)
    rotate(radians(-90))
    noFill()
    strokeWeight(6)
    if i < len(load):
        translate(-100,0)
        #print(i, len(load))
        stroke(255, 0, 0)
        r1 = map(disp[i] , min(disp), max(disp), 50, 250)
        circle(0,0, r1)
        
        stroke(0, 0, 244)
        r2 = map(load[i] , min(load), max(load), 50, 250)
        circle(0,0, r2)
        
        translate(100,0)
        strokeWeight(10)
        data_x.append(r2)
        data_y.append(r1)
        strokeWeight(1)
        
        for i in range(len(data_x)-1):
            line(data_x[i], data_y[i], data_x[i+1], data_y[i+1])
        
        
    else:
        end
    saveFrame("images/cycle9-######.png");
    i += 1
    
    
