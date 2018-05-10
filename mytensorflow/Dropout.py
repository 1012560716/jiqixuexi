#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据 one_hot 将数据转为一行
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

# 每个批次大小
batch_size = 100
# 计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size
# 定义两个 placeholder
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])
# 启用神经元百分比
keep_prob = tf.placeholder(tf.float32)
# 创建一个神经网络
# 输入层
# 权值
W1 = tf.Variable(tf.truncated_normal([784,1000],stddev=0.1))
b1 = tf.Variable(tf.zeros([1000])+0.1)
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)
# fropout 启动神经元百分比
L1_drop = tf.nn.dropout(L1,keep_prob)

# 隐藏层
W2 = tf.Variable(tf.truncated_normal([1000,1000],stddev=0.1))
b2 = tf.Variable(tf.zeros([1000])+0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop,W2)+b2)
L2_drop = tf.nn.dropout(L2,keep_prob)

W3 = tf.Variable(tf.truncated_normal([1000,500],stddev=0.1))
b3 = tf.Variable(tf.zeros([500])+0.1)
L3 = tf.nn.tanh(tf.matmul(L1_drop,W3)+b3)
L3_drop = tf.nn.dropout(L3,keep_prob)

# 输出层
W4 = tf.Variable(tf.truncated_normal([500,10],stddev=0.1))
b4 = tf.Variable(tf.zeros([10])+0.1)
prediction = tf.nn.softmax(tf.matmul(L3_drop,W4)+b4)

# 二次迭代函数
#loss = tf.readuce_mean(tf.square(y - prediction))
# 交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))

# 使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
# 初始化变量
init = tf.global_variables_initializer()
# 结果存放在一个布尔类型列表中
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1)) # argmax 返回最大值所在位置
# 求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(100):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.0})
        test_acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        train_acc = sess.run(accuracy, feed_dict={x: mnist.train.images, y: mnist.train.labels, keep_prob: 1.0})
        print("iter " + str(epoch) + "，Testing Accuracy " + str(test_acc) + ",Training_Accuracy "+str(train_acc) )