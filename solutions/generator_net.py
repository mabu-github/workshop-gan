from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers import Dense, BatchNormalization, LeakyReLU, Reshape, Conv2DTranspose

def build_generator_net_sln():
    return Sequential([
        # 100d vector to provide randomness
        # 1/16th of original size (1/4th for height, width) as low-resolution base image
        # capacity for 256 such base images
        Dense(7 * 7 * 256, use_bias=False, input_shape=(100,)),
        BatchNormalization(),

        # make it a 3d volume to be able to do convolutions
        Reshape((7, 7, 256)),

        Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False),
        LeakyReLU(),
        BatchNormalization(),

        # upsample to 14x14
        Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False),
        LeakyReLU(),
        BatchNormalization(),

        # upsample to 28x28
        Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'),
    ], name='generator')
