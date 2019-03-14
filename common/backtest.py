import pickle

from autoEncoder.autoEncoder import AutoEncoder
from cluster.Cluster import Cluster
from common.sharpe import SharpeRatio

# load the testing dataset
with open('../makeDataset/processedData/BackTestDict.pkl', 'rb') as f:
    data_set = pickle.load(f)

keys = list(data_set.keys())
max_len = len(data_set[keys[0]])

# load the encoder class
encoder = AutoEncoder()

# instantiate sharpe ratio calculator
sharpe = SharpeRatio()

# instantiate the clusterer
cluster = Cluster()

start = 1
end = start + 20


def get_twenty_days_data():
    global start
    global end
    global keys
    ret_val = dict()
    for key in keys:
        ret_val[key] = [x[0:5] for x in data_set[key][start:end]]  # OHLC

    start = end
    end = end + 20
    return ret_val


def calculate_returns(twenty_days_data):
    pass


def update_performance():
    pass


if __name__ == "__main__":
    while end < max_len:
        recent_data = get_twenty_days_data()
        for key in keys:
            if len(recent_data[key]) == 20:
                vector = encoder.get_vector(recent_data[key])

                recent_data[key] = vector


        clusters = cluster.generate_clusters(recent_data)
        print(clusters)
        break
