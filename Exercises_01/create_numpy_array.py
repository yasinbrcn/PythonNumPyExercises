"""
Created on Sun Oct 10 14:01:46 2021

@author: Yasin
"""

import numpy as np
key=1
numpy_array_values = []

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

def arrayYaz(r_numpy_array_values,r_data_type):
    numpy_array = np.array(r_numpy_array_values,dtype = r_data_type)
    print(numpy_array)
    print(type(numpy_array))
    
def oneDimArray():
    int_values = 0
    float_values = 0
    str_values = 0
    data_type = "none"
    value_number = int(input("How many values should be in the array?:"))
    
    for i in range (value_number):
        numpy_array_values.append(input(str(i) + ". Değeri Giriniz:"))
        try:
            numpy_array_values[i] = int(numpy_array_values[i])
            int_values = int_values + 1
        except:
            try:
                numpy_array_values[i] = float(numpy_array_values[i])
                float_values = float_values + 1
            except:
                str_values = str_values + 1
    if str_values > 0:
        data_type = "str"
        arrayYaz(numpy_array_values,data_type)
    elif float_values > 0:
        data_type = "float"
        arrayYaz(numpy_array_values,data_type)
    else:
        data_type = "int"
        arrayYaz(numpy_array_values,data_type)

def twoDimArray():
    raw_array = []
    row_value = int(input("Satır sayısını giriniz:"))
    column_value = int(input("Sütun sayısını giriniz:"))
    for j in range (1,(row_value+1)):
        for k in range (1,(column_value+1)):
            raw_array.append(input(str(j)+".satır"+str(k)+".sütun değerini giriniz:"))
    np_raw_array = np.array(raw_array,dtype="int")
    print(np_raw_array.reshape([row_value,column_value]))
    
    
'''
    array1 = []
    #np_array1 = []
    row_value = int(input("Satır sayısını giriniz:"))
    column_value = int(input("Sütun sayısını giriniz:"))
    for j in range (row_value):
        for k in range (column_value):
            array1.append(input(str(j)+".satır"+str(k)+".sütun değerini giriniz:"))
            if k == (column_value-1) and j == 0:
                np_array1 = np.array(array1,dtype="int")
                print("first")
                print(np_array1)
                array1.clear()
            elif k == (column_value-1):
                np_array2 = np.array(array1,dtype="int")
                print("second")
                print(np_array2)
                np_array1 = np.concatenate(([[np_array1,np_array2]]),dtype="int")
                print(np_array1)
                array1.clear()
    if j != "0":
        np_array2 = np.array(array1)
        print(np_array2)
        #np_array = np.concatenate([np_array1,np_array2],axis=1)
        #array1.clear()
    #print(np_array)
'''
while key == 1:    
    dim_array = int(input("Please enter the dimension of array:"))
    key = checkNumber(dim_array)
if dim_array == "1":
    oneDimArray()
else:
    twoDimArray()