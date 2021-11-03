"""
Created on Thu Oct 28 16:33:27 2021

@author: Yasin BİRCAN
"""

import numpy as np

key1 = 1
key2 = 1
numpy_array_values_1 = []
numpy_array_values_2 = []

def checkNumber(r_number):
    try:
        r_number = int(r_number)
        r_number_check = 0
    except:
        try:
            r_number = float(r_number)
            print("Please enter integer value only. Not float value.")
            r_number_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_number_check = 1
    return r_number_check

while key1 == 1:
    row1 = input("Please enter the row number of first array:")
    column1 = input("Please enter the column number of first array:")
    if checkNumber(row1) == 0 and checkNumber(column1) == 0:
        key1 = 0
    else:
        key1 = 1
row1 = int(row1)
column1 = int(column1)
row2 = row1
column2 = column1

for i in range (1,3):
    for j in range (1,(row1+1)):
        for k in range (1,(column1+1)):
            if i == 1:
                numpy_array_values_1.append(int(input("Please enter the "+str(j)+".row "+str(k)+".column value of "+str(i)+"st array:")))
            elif i == 2:
                numpy_array_values_2.append(int(input("Please enter the "+str(j)+".row "+str(k)+".column value of "+str(i)+"nd array:")))
        
np_raw_array_1 = np.array(numpy_array_values_1,dtype=int)
np_array_1 = np_raw_array_1.reshape([row1,column1])
print("Firs Array:" +"\n"+ str(np_array_1))
np_raw_array_2 = np.array(numpy_array_values_2,dtype=int)
np_array_2 = np_raw_array_2.reshape([row1,column1])
print("Second Array:" +"\n"+ str(np_array_2))

operation = str(input("Please select the operation you want to use:" +"\n"+ "[1]:Sum , [2]:Substract , [3]:Multiply , [4]:Divide --> "))
if operation == "1":
    print("Sum:" +"\n" + str(np.add(np_array_1,np_array_2)))
elif operation == "2":
    print("Substract:" +"\n" + str(np.subtract(np_array_1,np_array_2)))
elif operation == "3":
    print("Multiply:" +"\n" + str(np.multiply(np_array_1,np_array_2)))
elif operation == "4":
    print("Divide:" +"\n" + str(np.divide(np_array_1,np_array_2)))
else:
    print("Please select a valid operation!")