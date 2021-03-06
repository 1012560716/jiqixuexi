#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月14日
    BP 神经网络学习
'''

import numpy as np
# 输入数据
X = np.array([[1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]])
# 标签
Y = np.array([[0,1,1,0]])
# 权值初始化，取值范围 -1 到 1
V = np.random.random((3,4))*2-1
W = np.random.random((4,1))*2-1
print("初始 V 权值\n",V)
print("初始 W 权值\n",W)
# 学习速率设置
lr = 0.11
def sigmoid(x):
    # 激活函数 sigmoid 函数
    return 1/(1+np.exp(-x))
def dsigmoid(x):
    return x*(1-x)
def update():
    # 权值调整
    global X,Y,W,V,lr
    L1 = sigmoid(np.dot(X,V))   #隐藏层输出（4,4）
    L2 = sigmoid(np.dot(L1,W))   #输出层输出（4,1）
    #print("L1=",L1)
    #print("L2=", L2)
    L2_delta = (Y.T - L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)
    print("L2_delta=", L2_delta)
    #print("L1_delta=", L1_delta)
    #print("-"*30)
    W_C = lr * L1.dot(L2_delta)
    V_C = lr * X.T.dot(L1_delta)    # X 为 四行三列 L1_delta 为 四行四列，所以 X 需要转置才能相乘

    W = W + W_C
    V = V +V_C
for i in range(200000):
    update() # 更新权值
    if i%500==0:
        L1 = sigmoid(np.dot(X,V))   # 隐藏层输出（4,4）
        L2 = sigmoid(np.dot(L1,W))  # 输出层输出（4,1）
        #print("误差：",np.mean(np.abs(Y.T-L2)))
L1 = sigmoid(np.dot(X,V))   # 隐藏层输出（4,4）
L2 = sigmoid(np.dot(L1,W))  # 输出层输出（4,1）
print(L2)