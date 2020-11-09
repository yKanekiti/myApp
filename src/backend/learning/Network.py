from tensorflow.keras import layers, models, initializers

NUMBER_OF_FILTER_01 = 72
PADDING_SIZE_01 = 5
POOLING_SIZE_01 = 2
NUMBER_OF_FILTER_02 = 72
PADDING_SIZE_02 = 5
POOLING_SIZE_02 = 2
HIDDEN_SIZE = 4096


class Network:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

    def create_model(self):
        model = models.Sequential()

        model.add(layers.Reshape((self.input_size, self.input_size, 3), input_shape=(self.input_size * self.input_size,),
                                 name='reshape'))

        model.add(layers.Conv2D(NUMBER_OF_FILTER_01, (PADDING_SIZE_01, PADDING_SIZE_01), padding='same',
                                kernel_initializer=initializers.TruncatedNormal(),
                                use_bias=True, activation='relu',
                                name='conv_filter1'))
        model.add(layers.MaxPooling2D((POOLING_SIZE_01, POOLING_SIZE_01), name='max_pooling1'))

        model.add(layers.Conv2D(NUMBER_OF_FILTER_02, (PADDING_SIZE_02, PADDING_SIZE_02), padding='same',
                                kernel_initializer=initializers.TruncatedNormal(),
                                use_bias=True, activation='relu',
                                name='conv_filter2'))
        model.add(layers.MaxPooling2D((POOLING_SIZE_02, POOLING_SIZE_02), name='max_pooling2'))

        model.add(layers.Flatten(name='flatten'))
        model.add(layers.Dense(HIDDEN_SIZE, activation='relu',
                               kernel_initializer=initializers.TruncatedNormal(),
                               name='hidden'))
        model.add(layers.Dropout(rate=0.2, name='dropout'))
        model.add(layers.Dense(self.output_size, activation='softmax', name='softmax'))

        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['acc'])

        return model
