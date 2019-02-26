import pickle
import keras
from keras.layers import Dense, Input
from keras.layers import CuDNNLSTM
from keras.layers import TimeDistributed
from keras.models import Sequential
from numpy import array
import os

class AutoEncoder:
    def train(dataset):
        with open(dataset, 'rb') as f:
            sequence = pickle.load(f)
        sequence = array(sequence)
        sequence = sequence.reshape((len(sequence), 20, 4))
        #print(sequence.shape)

        model = Sequential()
        model.add(CuDNNLSTM(128, input_shape=(20, 4), return_sequences=True)) # encode 1
        model.add(CuDNNLSTM(256,  return_sequences=True)) # encode 2
        model.add(CuDNNLSTM(512,  return_sequences=True)) # encode 3 -- our final vector
        model.add(CuDNNLSTM(256,  return_sequences=True)) # decode 1
        model.add(CuDNNLSTM(128,  return_sequences=True)) # decode 2
        model.add(TimeDistributed(Dense(4)))
        model.compile(optimizer='adam', loss='mse')
 
        #print(model.summary())
        model.fit(sequence, sequence, epochs=1, batch_size=64, validation_split=0.2)
        model.save('model-latest.h5')
       # model.save('old-models/model-'+str(dataset))

    def get_vectors(data):
        #Load the latest model
        model = load_model('model-latest.h5')
        
        #Remove the decoder layer and set the model's output to the Encoder's output
        model = Model(inputs=model.inputs, outputs=model.layers[3].output)

        #Reshape the data
        sequence = array(data)
        sequence = sequence.reshape((len(sequence), 20, 4))

        #Run the model on the input timeseries and get vector representation
        vectors = model.predict(data)
        return vectors
        