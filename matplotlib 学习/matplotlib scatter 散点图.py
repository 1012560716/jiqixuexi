#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年4月1日
    绘制散点图
'''
import matplotlib.pyplot as plt
import numpy as np

#plt.scatter(np.arange(5),np.arange(5))

x = np.random.normal(0,1,500)
y = np.random.normal(0,1,500)
# s 点的大小 c 颜色 alpha 透明度
plt.scatter(x,y,s=50,c="b",alpha=0.5)
# 图像大小
plt.xlim((-2,2))
plt.ylim((-2,2))

# 取消尺度
#plt.xticks(())
#plt.yticks(())
plt.show()