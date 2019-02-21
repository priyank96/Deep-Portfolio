import matplotlib.pyplot as plt
from dtaidistance import dtw
from sklearn.cluster import DBSCAN
import pandas as pd

data_frame = pd.read_pickle("../pandafy/data.pkl").head(5).transpose().head(1000)     # need n_samples, n_features for algo
show_frame = pd.read_pickle("../pandafy/data.pkl").head(30).transpose().head(1000)     # need n_samples, n_features for algo
#data_frame.T.plot()
#plt.show()
print(data_frame.shape)

clustering = DBSCAN(eps=4, metric=dtw.distance_fast).fit(data_frame)

print(clustering.labels_.max())

for j in range(0, max(clustering.labels_)):
    zero = pd.DataFrame()
    for i in range(0, len(clustering.labels_)):
        if clustering.labels_[i] == j:
            zero = zero.append(show_frame.iloc[i])
    zero.T.plot()
    plt.show()
