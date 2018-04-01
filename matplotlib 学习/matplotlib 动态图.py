#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年4月1日
    绘制动态图
'''
import matplotlib.pyplot as plt
import numpy as np
# 导入动态图模块
from matplotlib import animation
fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

# 改变函数
def animate(i):
    line.set_ydata(np.sin(x*i/10))
    return line,
# 初始化函数
def init():
    line.set_ydata(np.sin(x))
    return line,
ani = animation.FuncAnimation(fig=fig,func=animate,init_func=init,interval=20)
plt.show()