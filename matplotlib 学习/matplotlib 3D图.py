#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年4月1日
    绘制3D图
'''
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 建一个视图
fig = plt.figure()
# 建一个3D视图
ax = Axes3D(fig)
# 取值，间隔0.25
x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
# 将X,Y传入网格中
X,Y = np.meshgrid(x,y)
# 定义Z 的值 sqrt 开平方
R = np.sqrt(X**2+Y**2)
# 对矩阵中的每个元素取正弦
Z = np.sin(R)
# rstride cstride 设置方块的大小 cmap 设置颜色
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap("rainbow"))
# 设置投影， zdir 投影在 z 轴上 offset 与原图的距离 cmap 颜色
ax.contourf(X,Y,Z,zdir="z",offset=-2,cmap="rainbow")
# 设置 z 轴的限制
ax.set_zlim(-2,2)
plt.show()
# 因为现实的图片不可以转动，所以可以在运行中搜索 ippython 然后将代码复制过去，shift+enter 执行
# 这样3D图就可以转动了