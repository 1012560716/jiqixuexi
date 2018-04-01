#!/usr/bin/env python
#-*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
# 将 x,y 传入网格之中
X,Y = np.meshgrid(x,y)
# comap 图的颜色 alphs 同名度
# 8 生成 8 个等高线
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
# 设置等高线的样式 colors 设置线的颜色 linewidth 设置线的粗细
C = plt.contour(X,Y,f(X,Y),8,colors="black",linewidth=0.5)
# 设置数值 inline 在线的里面 fontsize 字体大小
plt.clabel(C,inline=True,fontsize=10)
plt.xticks()
plt.yticks()
plt.show()