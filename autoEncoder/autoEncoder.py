# lstm autoencoder recreate sequence
import pickle

from keras.layers import Dense, Input
from keras.layers import LSTM
from keras.layers import TimeDistributed
from keras.models import Sequential
from numpy import array
import os

print(os.getcwd())

# define input sequence
with open("../makeDataset/processedData/FinalDataset.pkl", 'rb') as f:
    sequence = pickle.load(f)
sequence = array(sequence)
sequence = sequence.reshape((len(sequence), 20, 4))
print(sequence.shape)

# define model
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(20, 4), return_sequences=True))
model.add(LSTM(50, activation='relu', return_sequences=True))
model.add(LSTM(50, activation='relu', return_sequences=True))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(4)))
model.compile(optimizer='adam', loss='mse')

print(model.summary())
# fit model
model.fit(sequence, sequence, epochs=300, batch_size=64, validation_split=0.2)

# save the model weight in a model-weights folder
# do not delete old one, rename it by appending time stamp