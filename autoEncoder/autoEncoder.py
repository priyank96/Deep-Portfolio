import pickle

from keras.layers import CuDNNLSTM
from keras.layers import Dense
from keras.layers import TimeDistributed
from keras.models import Sequential, load_model, Model
from numpy import array


class AutoEncoder:

    def __init__(self):
        self.model = None
#        self.model_name = "model-latest.h5"
        self.model_name = "C:\\Users\\Admin\\Documents\\8th Sem Project\\Deep-Portfolio\\autoEncoder\\Blah.h5"

    def train(self, dataset):
        with open(dataset, 'rb') as f:
            sequence = pickle.load(f)
        sequence = array(sequence)
        sequence = sequence.reshape((len(sequence), 20, 4))
        # print(sequence.shape)

        model = Sequential()
        model.add(CuDNNLSTM(128, input_shape=(20, 4), return_sequences=True))  # encode 1
        model.add(CuDNNLSTM(256, return_sequences=True))  # encode 2
        model.add(CuDNNLSTM(512, return_sequences=True))  # encode 3 -- our final vector
        model.add(CuDNNLSTM(256, return_sequences=True))  # decode 1
        model.add(CuDNNLSTM(128, return_sequences=True))  # decode 2
        model.add(TimeDistributed(Dense(4)))
        model.compile(optimizer='adam', loss='mse')

        # print(model.summary())
        model.fit(sequence, sequence, epochs=1, batch_size=64, validation_split=0.2)
        model.save(self.model_name)

    # model.save('old-models/model-'+str(dataset))

    def get_vector(self, data):
        # Load the latest model
        if self.model is None:
            self.model = load_model(self.model_name)
            # Remove the decoder layer and set the model's output to the Encoder's output
            self.model = Model(inputs=self.model.inputs, outputs=self.model.layers[2].output) # TODO IMPORTANT FOR THE CURRENT MODEL IT IS 2

        # Reshape the data
        sequence = array(data)
        sequence = sequence.reshape(1, 20, 4)

        # Run the model on the input timeseries and get vector representation
        vectors = self.model.predict(sequence)
        print("shape: ",vectors.shape)
        return vectors
