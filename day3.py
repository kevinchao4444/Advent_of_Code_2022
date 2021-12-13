import numpy as np

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
    return decimal

array = []
with open("listday3.txt") as file_name:
    for line in file_name.readlines():
        x = line.strip('\n')
        array.append(x)

gamma = ''
epsilon = ''
strlen = len(array[0])

for i in range(strlen):
    count1 = 0
    count0 = 0

    for a in range(len(array)):
        if (array[a][i] == '0'):
            count0 += 1
        else:
            count1 += 1 
    if (count0 > count1):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

#print(gamma)
#print(epsilon)

gamma = binaryToDecimal(int(gamma))
epsilon = binaryToDecimal(int(epsilon))

print(gamma*epsilon)

#----------------------PART 2------------------------------------

array2 = array
temp = []
temp2 = []


while (len(array2) > 1):
    for i in range(len(array2[0])):
        count1 = 0
        count0 = 0

        for a in range(len(array2)):
            if (array2[a][i] == '0'):
                count0 += 1
                temp.append(array2[a])
            else:
                count1 += 1 
                temp2.append(array2[a])
        
