import numpy as np

with open("list.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

print(array)

for i in range(len(array)):
    list[i] = int(list[i])

print(array)

file_name.close()