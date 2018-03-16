#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月16日
    array 合并
'''
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([3,4,5])
arr3 = np.vstack((arr1,arr2))   # 垂直合并
print(arr3)
print(arr3.shape)

arr4 = np.hstack((arr1,arr2))   # 水平合并
print(arr4)
print(arr4.shape)

arrv = np.vstack((arr1,arr2,arr3))  # 垂直合并多个
print(arrv)

arrb = np.hstack((arr1,arr2,arr4))  # 水平合并多个
print(arrb)

arr = np.concatenate((arr1,arr2,arr1))  # 连接
print(arr)

arr = np.concatenate((arr3,arrv),axis=0)  # 合并的 array 纬度要相同，形状要匹配，axis = 0 纵向合并
print(arr)

arr = np.concatenate((arr3,arr3),axis=1)  # 合并的 array 纬度要相同，形状要匹配，axis = 1 横向合并

print(arr1.T)           # 一维的矩阵不能转置
print(arr1.shape)

# 增加矩阵纬度
arr1_1 = arr1[np.newaxis,:]     # 一维矩阵，变为 一行多列
print(arr1_1)
print(arr1_1.shape)
print(arr1_1.T)

arr1_2 = arr1[:,np.newaxis]     # 一维矩阵，变为 多行行一列
print(arr1_2)
print(arr1_2.shape)

arr1_3 = np.atleast_2d(arr1)    # 一维矩阵，变为 一行多列
print(arr1_3)

