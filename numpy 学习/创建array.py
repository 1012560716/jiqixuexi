#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月13日
    学习如何创建 array
'''
import numpy as np
a = np.array([1,2,3],dtype=np.int32)    # 创建 array 指定数据类型
print(a.dtype)
b = np.array([1,2,3],dtype=np.float)
print(b.dtype)
c = np.array([1,2,3])                   # 一维矩阵
print(c)
d = np.array([[1,2,3],                  # 二维矩阵
              [4,5,6]])
print(d)

zero = np.zeros((3,4))                  # 生成3行4列全都为0的矩阵
print(zero)
one = np.ones((3,4))                    # 生成3行4列全都为1的矩阵
print(one)
empty = np.empty((3,3))                 # 生成3行2列全都接近于0（不等于0）的矩阵
print(empty)
e = np.arange(10)                       # 生成一维 0-9 的矩阵
print(e)
f = np.arange(4,12)                     # 生成一维 4-11 的矩阵
print(f)
g = np.arange(1,20,3)                   # 生成 1-20 步长为 3 的一维矩阵
print(g)
h = np.arange(8).reshape(4,2)           # 生成 0-7 的二维 4行2列的矩阵  reshape 重新定义矩阵的形状
print(h)