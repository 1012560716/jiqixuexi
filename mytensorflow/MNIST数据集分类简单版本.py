#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

# 每个批次的大小
batch_size = 100
# 计算一共有多少个批次
n_batch = mnist.train.num_examples  // batch_size
# 定义两个 placeholder
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])
# 创建一个简单的神经网络
# 权值
W1 = tf.Variable(tf.zeros([784,10]))
# 偏置值
b1 = tf.Variable(tf.zeros([1,10]))

# F1 = tf.matmul(x,W1)+b1
# #激活函数
# L1 = tf.nn.tanh(F1)
# # 隐藏层
# W2 = tf.Variable(tf.random_normal([50,10]))
# b2 = tf.Variable(tf.zeros([1,10]))
prediction = tf.nn.softmax(tf.matmul(x,W1)+b1)

# 二次代价函数
# loss = tf.reduce_mean(tf.square(y-prediction))
# 交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
# 使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

#真实结果跟预测结果比较，结果存放在布尔型列表中
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))# argmax 返回一维张量中最大的值所在的位置
# 求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(100):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("lter "+ str(epoch)+",Testing Accuracy "+str(acc))