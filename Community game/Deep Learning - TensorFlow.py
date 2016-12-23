import random
import input_data


import tensorflow as tf

def main(argv):

    ################################
    # Enter your code between here #
    ################################

    mnist = input_data.read_data_sets(raw_input(), raw_input(), raw_input())

    # Start TF InteractiveSession
    sess = tf.InteractiveSession()

    # Build a Softmax Regression model
    ## Placeholders
    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])

    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(shape):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    W1 = weight_variable([784,100])
    b1 = bias_variable([100])
    W2 = weight_variable([100,300])
    b2 = bias_variable([300])
    W3 = weight_variable([300,10])
    b3 = bias_variable([10])

    ## Initializing Variables
    sess.run(tf.initialize_all_variables())

    # Prediction class and loss function
    keep_prob = tf.placeholder(tf.float32)
    h1 = tf.nn.relu(tf.matmul(x,W1) + b1)
    h2 = tf.nn.relu(tf.matmul(h1,W2) + b2)
    y = tf.nn.softmax(tf.matmul(h2,W3) + b3)

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    # Train model
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    for i in range(1000):
      batch = mnist.train.next_batch(100)
      train_step.run(feed_dict={x: batch[0], y_: batch[1]})


    # print ' '.join(map(str, [random.randint(0,9) for _ in range(len(mnist.validation.images))]))


    ########################
    #        And here      #
    ########################


    # Uncomment to get a prediction number for each image

    result = sess.run(tf.argmax(y,1), feed_dict={x: mnist.validation.images})
    print ' '.join(map(str, result))


if __name__ == '__main__':
    import sys
main(sys.argv[1:])