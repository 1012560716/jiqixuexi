#!/usr/bin/env python
#coding:utf-8
'''
    2018年3月25日
    matplotlib figure 图像学习
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,100)   # 生成 -1 到 1 的100值
y1 = 2*x+1
y2 = x**2

plt.figure()                # 一个 figure 显示一个图像  不写默认显示一个
plt.plot(x,y1)

plt.figure(figsize=(8,5))   # figsize 设置 figure 的大小
# 设置 x y 的显示范围
plt.xlim((-1,2))
plt.ylim((-2,3))

# 设置 x y 的描述
plt.xlabel('I AM X')
plt.ylabel("I AM Y")

# 设置 x y 轴上的刻度显示
new_ticks = np.linspace(-2,2,11)
plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ["level1","level2","level3","level4","level5"])# 两个列表，一个是刻度，一个是刻度替换的文字
# gca 获取坐标轴
ax = plt.gca()
# 设置坐标轴的颜色 none为去掉坐标轴
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")
# 将 x 轴和 y 轴设置为底部表框和左边边框
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# 设置 x 轴和 y 轴的位置
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
# 将显示的线赋值时，必须加 ，
l1, = plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--') # colot 颜色  linewidth 线的粗度，linestyle 线的样式
l2, = plt.plot(x,y1,color='blue',linewidth=5.0,linestyle="-")
# 设置图例  handles 需要设置的线，labels 对应线的描述，loc 图例的位置 best 自动寻找合适的位置
plt.legend(handles=[l1,l2],labels=["test1","test2"],loc="best")
plt.show()































