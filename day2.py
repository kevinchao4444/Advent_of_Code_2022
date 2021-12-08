import numpy as np

array = []
with open("listday2.txt") as file_name:
    for line in file_name.readlines():
        x = line.split(' ')
        y = int(x[1])
        z = [x[0], y]
        array.append(z)

#-------------PART ONE---------------------

#x_pos = 0
#y_pos = 0
#for i in range(len(array)):
#    if(array[i][0] == 'forward'):
#        x_pos += array[i][1]
#    elif(array[i][0] == 'down'):
#        y_pos += array[i][1]
#    elif(array[i][0] == 'up'):
#        y_pos -= array[i][1]


#--------------PART TWO----------------------

x_pos = 0
y_pos = 0
aim = 0
for i in range(len(array)):
    if(array[i][0] == 'forward'):
        if(aim!=0):
            y_pos += aim*array[i][1]
            x_pos += array[i][1]
        else:
            x_pos += array[i][1]
    elif(array[i][0] == 'down'):
        aim += array[i][1]
    elif(array[i][0] == 'up'):
        aim -= array[i][1]

print(x_pos*y_pos)