try:
    import tensorflow as tf
    print(tf.reduce_sum(tf.random.normal([1000, 1000])))
    print("Looks like Tensorflow is working as intended!")
except BaseException:
    print("It doesn't seem like Tensorflow is set up correctly.")
