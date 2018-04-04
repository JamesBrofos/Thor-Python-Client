from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from thor_client import ThorClient


# Load in the MNIST data.
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Create TensorFlow placeholders for the input, weights, biases, and output of
# the neural network.
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# Create TensorFlow elements in the computational graph corresponding to correct
# predictions, for total accuracy, and for the learning objective which is the
# binary cross entropy.
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Set the number of iterations that should elapse before we display progress.
n_prog = 1000


def mnist_logistic(lr, reg, n_batch, n_epochs):
    """This function estimates the parameters of a single-layer neural network
    for predicting class membership of handwritten digits. As input, it takes
    the learning rate, the regularization strength, the number of samples to use
    in a batch and the number of full passes through the dataset to perform
    (epochs).
    """
    # Create the loss function, which is the total of the cross entropy and the
    # regularization.
    loss = cross_entropy + reg * tf.reduce_sum(tf.square(W))
    # Train the model with stochastic gradient descent.
    train_step = tf.train.GradientDescentOptimizer(lr).minimize(loss)
    # The total number of iterations.
    # n_iters = (mnist.train.num_examples // n_batch) * n_epochs
    n_iters = n_epochs

    with tf.Session() as sess:
        # Initialize TensorFlow.
        sess.run(tf.global_variables_initializer())
        # Perform learning iterations.
        for _ in range(n_iters):
            if _ % n_prog == 0:
                print("Progress: {} / {}.".format(_ + 1, n_iters))
            batch_xs, batch_ys = mnist.train.next_batch(n_batch)
            sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        # At the end of the learning sequence, return the accuracy on the test
        # set of images.
        return sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})


# Create experiment.
tc = ThorClient()
dims = [
    {"name": "learning rate", "dim_type": "logarithmic", "low": 1e-8, "high": 1.},
    {"name": "regularizer", "dim_type": "linear", "low": 0., "high": 1.},
    {"name": "batch size", "dim_type": "integer", "low": 20, "high": 2000},
    {"name": "epochs", "dim_type": "integer", "low": 5, "high": 20000}
]
exp = tc.create_experiment("MNIST Logistic Regression", dims, overwrite=True)

# Main optimization loop.
for i in range(100):
    # Request new recommendation.
    rec = exp.create_recommendation()
    c = rec.config
    # Evaluate new recommendation.
    val = mnist_logistic(
        c["learning rate"], c["regularizer"], c["batch size"], c["epochs"]
    )
    # Submit recommendation.
    rec.submit_recommendation(val)



