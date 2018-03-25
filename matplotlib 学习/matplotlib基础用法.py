#!/usr/bin/env python
#coding:utf-8
'''
    2018年3月25日
    matplotlib 绘图工具的使用
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)   # 从 -1 到 1 生成 100个点
y = 2*x+1
plt.plot(x,y)               # 传入 x值和y值
plt.show()                  # 显示图像