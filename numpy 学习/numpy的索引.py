#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月16日
    numpy 的索引
    和列表的操作差不多
'''
import numpy as np
arr1 = np.arange(2,14)
print(arr1)

print(arr1[2])      # 第二个位置的数据
print(arr1[1:4])    # 第一到第四个位置的数据
print(arr1[2:-1])   # 第二到倒数第一个位置的数据
print(arr1[:5])     # 前五个数据

arr2 = arr1.reshape(3,4)    # 重新形成矩阵形状
print(arr2)

print(arr2[1])        # 矩阵坐标从 0 开始，表示矩阵第二行
print(arr2[1][1])       # 第二行，第二列
print(arr2[1,1])

print(arr2[:,2])    # 第三列

for i in arr2:      # 迭代行
    print(i)


for i in arr2.T:    # 迭代列
    print(i)

for i in arr2.flat: # 迭代每一个元素
    print(i)