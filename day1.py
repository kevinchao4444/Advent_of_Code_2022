import numpy as np

with open("listday1.txt") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

print(array)
count = 0


for i in range(len(array)-1):
    temp = array[i+1]
    if (temp > array[i]):
        count += 1

print(count)

count = 0

sum_a = 0
sum_b = 0
for i in range(len(array)-3):
    sum_a = array[i] + array[i+1] + array[i+2]
    sum_b = array[i+1] + array[i+2] + array[i+3]
    if (sum_b > sum_a):
        count += 1

print(count)

file_name.close()