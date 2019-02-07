import pandas as pd
from scipy.spatial import distance
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

# use normalized data
initial = pd.read_pickle("../pandafy/data.pkl")
volume_initial = pd.read_pickle("../pandafy/volume_data.pkl")

n_minutes = 100
n_lines = 5
extra_plot = 1000
max_dist = 2.0

sliced_frame = initial.head(n_minutes)
volume_sliced_frame = volume_initial.head(n_minutes)

double_sliced_frame = initial.head(extra_plot*n_minutes)
volume_double_sliced_frame = volume_initial.head(extra_plot*n_minutes)

# pick one column at random
random_column_index = initial.columns.to_series().sample(1)
reference_column = initial[random_column_index]
volume_reference_column = volume_initial[random_column_index]


print(sliced_frame.head())
print(volume_sliced_frame.head())

sliced_reference_column = reference_column[:n_minutes]
double_sliced_reference_column = reference_column[:extra_plot*n_minutes]

volume_sliced_reference_column = volume_reference_column[:n_minutes]
volume_double_sliced_reference_column = volume_reference_column[:extra_plot*n_minutes]


# apply similarity on first n minutes
def sqeuclidean(t1, t2):
    """pairwise square euclidean distance of numpy arrays or lists"""
    return distance.sqeuclidean(t1, t2)


def volume_similarity(n_closest):
    global n_minutes
    global reference_column
    global sliced_frame
    global max_dist
    list_distances = []
    for column in sliced_frame:
        dist = (sqeuclidean(sliced_reference_column, sliced_frame[column]) +
                sqeuclidean(volume_sliced_reference_column, volume_sliced_frame[column]))**0.5

        if dist < max_dist or True:
            list_distances.append((column, dist))

    return sorted(list_distances, key=itemgetter(1))[1:n_lines]


# apply similarity on first n minutes
def euclidean(t1, t2):
    """pairwise euclidean distance of numpy arrays or lists"""
    return distance.euclidean(t1, t2)


def similarity(n_closest):
    global n_minutes
    global reference_column
    global sliced_frame
    global max_dist
    list_distances = []
    for column in sliced_frame:
        dist = euclidean(sliced_reference_column, sliced_frame[column])
        if dist < max_dist:
            list_distances.append((column, dist))

    return sorted(list_distances, key=itemgetter(1))[1:n_lines]


# plot n closest for 2n minutes
def plot(indices_tuples_list):
    global double_sliced_frame
    global double_sliced_reference_column
    for tuple_column_dist in indices_tuples_list:
        plt.plot(double_sliced_frame[tuple_column_dist[0]])
    plt.plot(sliced_reference_column, linewidth=3.5)


if __name__ == "__main__":
    plt.ion()
    for i in range(5, 200):
        n_minutes = i
        sliced_frame = initial.head(n_minutes)
        double_sliced_frame = initial.head(extra_plot * n_minutes)
        sliced_reference_column = reference_column[:n_minutes]
        double_sliced_reference_column = reference_column[:extra_plot * n_minutes]

        list_tuples = volume_similarity(n_lines)
        # ax1 = plt.subplot(211)
        plt.yticks(np.arange(-2, 2, 0.1))
        plot(list_tuples)

        # list_tuples = similarity(n_lines)
        # plt.subplot(212, sharex=ax1, sharey=ax1)
        # plt.yticks(np.arange(-2, 2, 0.1))
        # plot(list_tuples)

        plt.pause(0.01)
        plt.clf()
