#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月13日
    线性神经网络代码实现

    异或问题
    1 1 = 0
    0 0 = 0
    1 0 = 1
    0 1 = 1

'''
import numpy as np
import matplotlib.pyplot as plt

# 输入数据
X = np.array([[1,1,1,1,1,1],
             [1,0,0,0,0,0],
             [1,1,0,1,0,0],
              [1,0,1,0,0,1]])
# 标签
Y = np.array([-1,-1,1,1])
# 权值初始化，一行三列，取值范围 -1到1
W = ((np.random.random(6)-0.5)*2)
print(W)
# 学习率设置
lr = 0.11
# 计算迭代次数
n = 0
# 神经网路输出
O = 0
def updata():
    global X,Y,W,lr,n
    n +=1
    O = np.dot(X,W.T)
    W_C = lr*((Y-O.T).dot(X))/int(X.shape[0])
    W = W + W_C
    return O
# 迭代
def iteration():
    for i in range(1000):
        updata() # 得到当前输出
def calculate(x,root):
    a = W[5]
    b = W[2]+x*W[4]
    c = W[0]+x*W[1]+x*x*W[3]
    if root ==1:
        return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:
        return (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
if __name__ == "__main__":
    iteration()
    print(updata())
    # 正样本
    x1 = [1, 0]
    y1 = [0, 1]
    # 负样本
    x2 = [1, 0]
    y2 = [1, 0]
    xdata = np.linspace(-1,2)
    plt.figure()
    plt.plot(xdata,calculate(xdata,1),"r")
    plt.plot(xdata, calculate(xdata, 2), "r")
    plt.plot(x1,y1,'bo')
    plt.plot(x2,y2,"yo")
    plt.show()