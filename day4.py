import numpy as np

array = []
bingonumbers = []
with open("listday4.txt") as file_name:
    bingonumbers = file_name.readline()
    bingonumbers = bingonumbers.strip('\n').split(',')
    for line in file_name.readlines():
        x = line.strip('\n')
        array.append(x)


print(array)
