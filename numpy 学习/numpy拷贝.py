#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月16日
    numpy 的浅拷贝和深拷贝
'''
import numpy as np
arr1 = np.array([1,2,3])
arr2 = arr1 # 直接用 = 号，只是复制的内存地址，arr1 和 arr2 公共一块内存，修改一个，同时会修改另一个

arr3 = arr1.copy() # 深拷贝 修改其中一个，不会对另一个有影响