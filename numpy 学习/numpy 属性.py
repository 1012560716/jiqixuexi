#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月13日
    numpy 常用属性学习
'''
import numpy as np
arr1 = np.array([[1,2,3],
          [4,5,6]])
print(arr1.ndim)    # 矩阵纬度
print(arr1.dtype)   # 类型
print(arr1.shape)   # 矩阵几行几列
print(arr1.size)    # 矩阵长度
