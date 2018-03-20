#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
    2018年3月19日
    用 BP 算法识别数字图片
    3 层网络
    输入层——隐藏层——输出层

'''

import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import  train_test_split

# 激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))
# sigmoid 的导数
def dsigmoid(x):
    return x*(1-x)

class NeuralNetwork(object):
    def __init__(self,layers): #(64,100,10)
        # 权值的初始化，范围 -1 到 1
        self.V = np.random.random((layers[0]+1,layers[1]+1))*2-1
        self.W = np.random.random((layers[1] + 1, layers[2])) * 2 - 1

    def train(self,X,y,lr=0.11,epochs=10000):
        # 添加偏置
        temp = np.ones([X.shape[0],X.shape[1]+1])
        temp[:,0:-1] = X
        X = temp

        for n in range(epochs+1):
            i = np.random.randint(X.shape[0])   # 随机选取一个数据
            x = [X[i]]
            x = np.atleast_2d(x)    # 将 一维数据转为 二维数据

            L1 = sigmoid(np.dot(x,self.V))  # 隐藏层输出
            L2 = sigmoid(np.dot(L1, self.W))  # 隐藏层输出

            L2_dalta = (y[i]-L2)*dsigmoid(L2)
            L1_dalta = L2_dalta.dot(self.W.T)*dsigmoid(L1)

            self.W += lr*L1.T.dot(L2_dalta)
            self.V += lr * x.T.dot(L1_dalta)

            # 每训练 1000 次 预测一次准确率
            if n% 1000 ==0:
                predictions = []
                for j in range(X_test.shape[0]):
                    o = self.predict(X_test[j])
                    predictions.append(np.argmax(o))    # 获取预测结果
                accuracy = np.mean(np.equal(predictions,y_test))
                print("epoch:",n,"accuracy:",accuracy)
    def predict(self,x):
        # 添加偏置
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        x = temp
        x = np.atleast_2d(x)    # 转为二维数据
        L1 = sigmoid(np.dot(x, self.V))  # 隐藏层输出
        L2 = sigmoid(np.dot(L1, self.W))  # 隐藏层输出
        return L2
digits = load_digits()  # 载入数据集
X = digits.data     # 数据
y = digits.target   # 标签

# 输入数据归一化
X -=X.min()
X /=X.max()

nm = NeuralNetwork([64,100,10]) #创建网络
X_train,X_test,y_train,y_test = train_test_split(X,y)   # 分割数据，训练数据：测试数据 = 1:3

labels_train = LabelBinarizer().fit_transform(y_train)  # 标签二值化
labels_test = LabelBinarizer().fit_transform(y_test)  # 标签二值化

print("开始")

nm.train(X_train,labels_train,epochs=20000)

print("结束")


