from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers import Dense, LeakyReLU, Conv2D, Dropout, Flatten


def build_discriminator_net_sln():
    return Sequential([
        Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=(28, 28, 1)),
        LeakyReLU(),
        Dropout(0.3),

        Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
        LeakyReLU(),
        Dropout(0.3),

        Flatten(),
        Dense(1, activation='sigmoid'),
    ], name='discriminator')
