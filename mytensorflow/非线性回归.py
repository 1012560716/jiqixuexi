#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 使用 numpy 生成200个随机点 并增加一个维度，转完成 200行1列
x_data = np.linspace(-0.5,0.5,10)[:,np.newaxis]
# 生成噪点 形状和 x_data 一样
noise = np.random.normal(0,0.02,x_data.shape)
# y = x**2 + b
y_data = np.square(x_data) + noise

# 定义两个 placeholder
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

# 定义神经网络中间层
# 参数矩阵
Weights_L1 = tf.Variable(tf.random_normal([1,10]))
# 偏置值
biases_l1 = tf.Variable(tf.zeros([1,10]))
# 矩阵相乘 + 偏置值
Wx_plus_b_L1 = tf.matmul(x,Weights_L1) + biases_l1
# 激活函数
L1 = tf.nn.tanh(Wx_plus_b_L1)
L3 = tf.nn.tanh(x)

# 定义神经网络输出层
Weights_L2 = tf.Variable(tf.random_normal([10,1]))
biases_l2 = tf.Variable(tf.zeros([1,1]))
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2) + biases_l2
prediction = tf.nn.tanh(Wx_plus_b_L2)

# 二次代价函数
loss = tf.reduce_mean(tf.square(y - prediction))
# 使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
with tf.Session() as sess:
    # 变量初始化
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        sess.run(train_step,feed_dict = {x:x_data,y:y_data})

    # 获得预测值
    #prediction_value = sess.run(prediction,feed_dict = {x:x_data})
    print(sess.run(L3,feed_dict={x:[[5]]}))
    # 画图
    plt.figure()
    plt.scatter(x_data,y_data)
    #plt.plot(x_data,prediction_value,"r",lw=5)
    plt.show()
