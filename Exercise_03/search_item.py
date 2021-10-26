"""
Created on Sun Oct 17 18:46:27 2021

@author: Yasin BİRCAN
"""
import random
import numpy as np
key=1
counter = 0
limit_1 = 0
limit_2 = random.randint(50,100)
row = random.randint(50,100)
column = random.randint(50,100)

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

while key == 1:
    search_value = input("Please enter the value to be searched for:")
    key = checkNumber(search_value)
    
numpy_array = np.random.randint(limit_1,limit_2,(row,column))
print("NUMPY ARRAY:")
print(numpy_array)
print("INDEX LIST:")
for i in range (row):
    for j in range (column):
        if numpy_array[i,j] == int(search_value):
            print("["+str(i)+","+str(j)+"] = " + str(search_value))
            counter = counter + 1
        else:
            counter = counter
print("Numpy array consists of " + str(row) + " rows and " + str(column) + " columns.")
print("The value " + str(search_value) + " appears " + str(counter) + " times in the array.")