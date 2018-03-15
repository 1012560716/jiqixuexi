#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月15日
    生成随机数矩阵
'''
import numpy as np
sample = np.random.random((3,2))    # 生成3行2列从0到1的随机数
print(sample)

sample2 = np.random.normal(size=(3,2))  # 生成3行2列符合标准正态分布的随机数
print(sample2)

sample3 = np.random.randint(0,10,size=(3,2))    # 生成3行2列从0到10的随机数
print(sample3)

print(np.sum(sample))   # 求和
print(np.min(sample))   # 求最小值
print(np.max(sample))   # 求最大值

print(np.sum(sample,axis=0))    # 对列求和
print(np.sum(sample,axis=1))    # 对行求和

print(np.argmin(sample))    # 求最小值的索引
print(np.argmax(sample))    # 求最大值的索引

print(np.mean(sample))      # 求平均值
print(sample.mean())        # 求平均值

print(np.median(sample))    # 求中位数

print(sample)
print(np.sqrt(sample))      # 开方

sample4 = np.random.randint(0,10,size=(1,10))
print(sample4)
print(np.sort(sample4))     # 排序

print(np.clip(sample4,2,7)) # 判断小于2 的改成2，大于7的改成7