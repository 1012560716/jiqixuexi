#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月28日
    matplotlib 标注的学习
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y1 = 2*x+1
plt.plot(x,y1,color="red",linewidth=1.0,linestyle='-')
# 获取坐标轴
ax = plt.gca()
# 去掉右边和上边边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将x轴设为底边框
# 将y轴设为左边框
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# 设置 底边对应到0点
# 设置 左边对应到0点
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 0.5
y0 = 2*x0 + 1
# 标点
plt.scatter(x0,y0,s=50,color='b')
# 画虚线
plt.plot([x0,x0],[y0,0],'k--',lw=2)

# xy 对应标记的点
#xytext 文字描述的位置 +30 -30 以标记点 在 x 轴 方向+30，y 轴 方向-30
# textcoords 代表标记点作为起点
# arrowprops 加上箭头
# connectionstyle 箭头的样式 arc 箭头的样式 rad 箭头的弧度'arc3,rad=0.2
plt.annotate(r"$2x+1=%s$" %y0,xy=(x0,y0),xytext=(+30,-30),textcoords="offset points",fontsize=16,
             arrowprops = dict(arrowstyle="->",connectionstyle='arc3,rad=0.2'))
# 文字描述 在 -1,2 的位置开始
plt.text(-1,2,r'$thsi\ is\ the\ text$',fontdict={"size":"16","color":"r"})
plt.show()