#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月13日
    numpy 的运算
    + - * ** / % // 都是按位运算，需要矩阵形状相同
'''
import numpy as np
arr1 = np.array([[1,2,3],
                 [4,5,6]])
arr2 = np.array([[1,1,2],
                 [2,3,3]])
print(arr1)
print(arr2)
print(arr1+arr2)    # 加法
print(arr1-arr2)    # 减法
print(arr1*arr2)    # 乘法
print(arr1**arr2)   # 幂运算
print(arr1/arr2)    # 除法
print(arr1%arr2)    # 取余
print(arr1//arr2)   # 取整
print(arr1+2)       # 所有元素+2
print(arr1*10)      # 所有元素*10
print(arr1>3)       # 判断哪些元素大于3

arr3 = np.ones((3,5))
print(np.dot(arr1,arr3))    # 矩阵乘法运算 注意 第一个矩阵的列数与第二个矩阵的行数相同才能运算
print(arr1.dot(arr3))

print(arr1.T)           #矩阵转置
print(np.transpose(arr1))
