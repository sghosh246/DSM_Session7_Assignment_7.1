# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:05:49 2018
@author: souravg
"""
"""
Write a function to find moving average in an array over a window Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
"""
import numpy as np
def moving_avg(array,window =3):
    out_arr = np.array([])
    '''
    Passing a defined list to a function, initialize an empty array, iterating the passed input list for each element till n-k+1(length of list - window size + 1 ), adding three consecutive elements strating from index = 0 and dividing by window size of 3
    and pushing that calculated value inside that blank array. Once the loop iteration is over function returns the array with appended values.
    '''
    for i in range(len(array)-window+1): 
        sliced_arr = sum(array[i:window+i])/window
        out_arr = np.append(out_arr,sliced_arr)
    return out_arr
list = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
array = np.array(list)
print(moving_avg(array))