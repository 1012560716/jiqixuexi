#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月12日
    单感知器代码实现

    异或问题
    1 1 = 0
    0 0 = 0
    1 0 = 1
    0 1 = 1

'''
import numpy as np
import matplotlib.pyplot as plt

# 输入数据
# X = np.array([[1,3,3],
#              [1,4,3],
#              [1,1,1],
#               [1,3,4]])
X = np.array([[1,1,1],
             [1,0,0],
             [1,1,0],
              [1,0,1]])
# 标签
Y = np.array([0,0,1,1])
# 权值初始化，一行三列，取值范围 -1到1
W = ((np.random.random(3)-0.5)*2)
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
    O = np.sign(np.dot(X,W.T))
    W_C = lr*((Y-O.T).dot(X))/int(X.shape[0])
    W = W + W_C
    return O
# 迭代
def iteration():
    for i in range(100):
        O = updata() # 得到当前输出
        print(O)
        print(W) # 打印当前权值
        print(n) # 打印迭代次数
        if ( O == Y.T).all(): # 如果实际输出等于期望输出，得到收敛 循环结束
            print("Finished")
            print("迭代次数",n)
            break
if __name__ == "__main__":
    iteration()
    # 正样本
    # x1 = [3,4,3]
    # y1 = [3,3,4]
    # 负样本
    # x2 = [1]
    # y2 = [1]

    # 正样本
    x1 = [1, 0]
    y1 = [0, 1]
    # 负样本
    x2 = [1, 0]
    y2 = [1, 0]
    # 计算分界线的斜率以及截距
    k = -W[1]/W[2]
    d = -W[0]/W[2]
    print("k=",k)
    print("d=",d)

    xdata = np.linspace(-2,5)
    plt.figure()
    plt.plot(xdata,xdata*k+d,"r")
    plt.plot(x1,y1,'bo')
    plt.plot(x2,y2,"yo")
    plt.show()