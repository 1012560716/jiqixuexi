#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年4月1日
    设置子视图
'''
import matplotlib.pyplot as plt
import numpy as py
# 建一个视图
plt.figure()
# 设置子视图 两行一列 第一个位置
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
# 设置子视图 两行一列 第3个位置 由于第一个子视图占了两个位置
plt.subplot(2,2,3)
plt.plot([0,1],[0,1])
plt.subplot(2,2,4)
plt.plot([0,1],[0,1])
plt.show()