import pickle
from autoEncoder.autoEncoder import AutoEncoder
# load the testing dataset
with open('../makeDataset/processedData/BackTestDict.pkl') as f:
    data_set = pickle.load(f)

def get_full_historical_data():
    pass

def get_twenty_days_data():
    pass

def calculate_returns():
    pass

def update_performance():
    pass

# load the encoder class
encoder = AutoEncoder()

# start from 21st day in the dataset


# vectorize last 20 days data
# cluster the vectors


