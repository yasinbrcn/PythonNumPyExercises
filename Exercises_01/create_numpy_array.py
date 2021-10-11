"""
Created on Sun Oct 10 14:01:46 2021

@author: Yasin BİRCAN
"""

import numpy as np
key=1
key2=1

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

def writeArray(r_numpy_array_values,r_data_type,rw_row_value,rw_column_value):
    np_raw_array = np.array(r_numpy_array_values,dtype=r_data_type)
    np_array = np_raw_array.reshape([rw_row_value,rw_column_value])
    print(np_array)

def createNumpyArray(r_row_value,r_column_value):
    numpy_array_values = []
    int_values = 0
    float_values = 0
    str_values = 0
    data_type = "none"
    r_row_value = int(r_row_value)
    r_column_value = int(r_column_value)
    
    for j in range (1,(r_row_value+1)):
        for k in range (1,(r_column_value+1)):
            numpy_array_values.append(input("Please enter the "+str(j)+".row "+str(k)+".column value:"))
    for l in range((r_row_value*r_column_value)):
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
        writeArray(numpy_array_values,data_type,r_row_value,r_column_value)
    elif float_values > 0:
        data_type = "float"
        writeArray(numpy_array_values,data_type,r_row_value,r_column_value)
    else:
        data_type = "int"
        writeArray(numpy_array_values,data_type,r_row_value,r_column_value)
      
while key == 1:    
    row_value = input("Please enter a row number:")
    key = checkNumber(row_value)
while key2 == 1:
    column_value = input("Please enter a column number:")
    key2 = checkNumber(column_value)
createNumpyArray(row_value,column_value)