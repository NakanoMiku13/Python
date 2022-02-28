
#import tensorflow as tf
#w1 = tf.Variable(tf.random.normal(shape=[2]), name='w1')
#w2 = tf.Variable(tf.random.normal(shape=[5]), name='w2')
#saver = tf.train.Saver()
#sess = tf.Session()
#sess.run(tf.global_variables_initializer())
#saver.save(sess, 'my_test_model')
import os

import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)