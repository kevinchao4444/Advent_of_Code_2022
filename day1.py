import numpy as np

with open("list.txt") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

print(array)

for i in range(len(array)):
    temp = array[i]
    array[i] = int(temp)

print(array)

file_name.close()