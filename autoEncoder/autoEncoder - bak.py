import pickle
import keras
from keras.layers import Dense, Input
from keras.layers import CuDNNLSTM
from keras.layers import TimeDistributed
from keras.models import Sequential
from numpy import array
import os

# lstm autoencoder recreate sequence

# define input sequence
with open("../makeDataset/processedData/FinalDataset.pkl", 'rb') as f:
    sequence = pickle.load(f)
sequence = array(sequence)
sequence = sequence.reshape((len(sequence), 20, 4))
print(sequence.shape)

# define model
model = Sequential()
model.add(CuDNNLSTM(128, input_shape=(20, 4), return_sequences=True)) # encode 1
model.add(CuDNNLSTM(256,  return_sequences=True)) # encode 2
model.add(CuDNNLSTM(512,  return_sequences=True)) # encode 3 -- our final vector
model.add(CuDNNLSTM(256,  return_sequences=True)) # decode 1
model.add(CuDNNLSTM(128,  return_sequences=True)) # decode 2
model.add(TimeDistributed(Dense(4)))
model.compile(optimizer='adam', loss='mse')
 
print(model.summary())
# fit model
model.fit(sequence, sequence, epochs=300, batch_size=64, validation_split=0.2)

#model.save('model-latest.h5')
#del model

#from keras.models import load_model

#model = load_model('model-latest.h5')
#model.fit(sequence[0:1], sequence[0:1], epochs=1, batch_size=64)



#print(sequence[0:1])
#print(model.predict(sequence[0:1]))

#for lay in model.layers:
#    print(lay.name)
#    print(lay.get_weights())




# save the model weight in a model-weights folder
# do not delete old one, rename it by appending time stamp