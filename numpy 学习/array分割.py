#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月16日
    array分割
    split分割为平均分割，如果无法分割，会报错
    array_split 可以不等分割
'''
import numpy as np
arr1 = np.arange(12).reshape((3,4))
print(arr1)

arr2,arr3 = np.split(arr1,2,axis=1) # 水平方向分割，分成两份
print(arr2)
print(arr3)

arr4,arr5,arr6 = np.split(arr1,3,axis=0) # 垂直方向分割，分成3份
print(arr4)
print(arr5)
print(arr6)

arr7,arr8,arr9 = np.array_split(arr1,3,axis=1) # 水平方向分割，分成3份，不等分割
print(arr7)
print(arr8)
print(arr9)

arrv1,arrv2,arrv3 = np.vsplit(arr1,3)   # 垂直分割
print(arrv1)
print(arrv2)
print(arrv3)

arrh1,arrh2= np.hsplit(arr1,2)          # 水平分割
print(arrh1)
print(arrh2)