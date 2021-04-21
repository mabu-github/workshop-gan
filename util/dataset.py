import tensorflow as tf
import numpy as np


def load_mnist_data():
    """ Returns data as (train_images, train_labels), (test_images, test_labels) """
    return prepare_data(tf.keras.datasets.mnist)


def prepare_data(dataset):
    (train_images, train_labels), (test_images, test_labels) = dataset.load_data()

    train_images = (train_images.reshape(-1, 28, 28, 1) / 127.5 - 1).astype(np.float32)
    test_images = (test_images.reshape(-1, 28, 28, 1) / 127.5 - 1).astype(np.float32)

    return (train_images, train_labels), (test_images, test_labels)
