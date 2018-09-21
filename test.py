# _-*- coding: utf-8 -*-
"""
@author: cx
@data: 0912

"""
import numpy as np

def doubleArray(arr):
    #对数组的每个元素进行翻倍
    
    arr = np.array(arr)

    return arr*2

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(doubleArray(arr))


