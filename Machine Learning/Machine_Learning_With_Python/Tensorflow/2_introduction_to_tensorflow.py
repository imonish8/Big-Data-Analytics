import tensorflow as tf

t = tf.ones([5, 5, 5])
print(t)

reshaped_t = tf.reshape(t, [125])
print("\nReshaped t ")
print(reshaped_t)