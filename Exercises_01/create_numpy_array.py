"""
Created on Sun Oct 10 14:01:46 2021

@author: Yasin
"""

import numpy as np
key=1

def checkNumber(r_number):
    try:
        r_number = int(r_number)
        if r_number >= 1 and r_number <= 8:
            r_number_check = 0
        else:
            print("Please enter between 1-8")
            r_number_check = 1
    except:
        try:
            r_number = float(r_number)
            print("Please enter between 1-8")
            r_number_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_number_check = 1
    return r_number_check

def writeArray(r_numpy_array_values,r_data_type,r_row_value,r_column_value):
    np_raw_array = np.array(r_numpy_array_values,dtype=r_data_type)
    np_array = np_raw_array.reshape([r_row_value,r_column_value])
    print(np_array)
    print(np_array.ndim)

def createNumpyArray():
    numpy_array_values = []
    int_values = 0
    float_values = 0
    str_values = 0
    data_type = "none"
    row_value = int(input("Satır sayısını giriniz:"))
    column_value = int(input("Sütun sayısını giriniz:"))
    for j in range (1,(row_value+1)):
        for k in range (1,(column_value+1)):
            numpy_array_values.append(input(str(j)+".satır "+str(k)+".sütun değerini giriniz:"))
    for l in range((row_value*column_value)):
        try:
            numpy_array_values[l] = int(numpy_array_values[l])
            int_values = int_values + 1
        except:
            try:
                numpy_array_values[l] = float(numpy_array_values[l])
                float_values = float_values + 1
            except:
                str_values = str_values + 1
    if str_values > 0:
        data_type = "str"
        writeArray(numpy_array_values,data_type,row_value,column_value)
    elif float_values > 0:
        data_type = "float"
        writeArray(numpy_array_values,data_type,row_value,column_value)
    else:
        data_type = "int"
        writeArray(numpy_array_values,data_type,row_value,column_value)
      
while key == 1:    
    dim_array = int(input("Please enter the dimension of array:"))
    key = checkNumber(dim_array)
createNumpyArray()