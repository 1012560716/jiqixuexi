#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年4月1日
    绘制直方图
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = 2**x+10
# -y 直方图会倒过来
#facecolor 颜色
# edgecolor 边框颜色
plt.bar(x,y,facecolor="#9999ff",edgecolor="white")
for x,y in zip(x,y):
    # ha va 数值的显示位置 va = "top" 显示在顶部的下面
    plt.text(x,y,'%0.2f'% y,ha='center',va ='bottom')
plt.show()