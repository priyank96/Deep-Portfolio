import community
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity as cosine


class Cluster:
    def generate_clusters(self, to_cluster):

        instruments = list(to_cluster.keys())
        similarity_measures = dict()  # key is 2 instruments, value is cosine similarity
        for i in range(0, len(instruments) - 1):
            for j in range(i + 1, len(instruments)):
                similarity_measures[tuple([instruments[i], instruments[j]])] = cosine(
                    to_cluster[instruments[i]], to_cluster[instruments[j]])[0][0]
        G = nx.Graph()
        G.add_nodes_from(instruments)

        for edge in similarity_measures.keys():
            edge_tuple = list(edge)
            # edge_tuple.append({'weight' : similarity_measures[edge]})
            G.add_edge(edge_tuple[0], edge_tuple[1], weight=similarity_measures[edge])

        print(G)
        communities = community.best_partition(G)
        return communities


if __name__ == "__main__":
    cluster = Cluster()
    print("Running Test#1  for Clustering")
    test1_dict = {"a": [[1, 2, 3], [1, 2, 3]], "b": [[90, 9, 9], [90, 9, 9]], "c": [[1, 1, 3], [1, 1, 3]],
                  "d": [[90, 8, 8], [90, 8, 8]]}
    print(test1_dict)

    print(cluster.generate_clusters(test1_dict))

    print("Running Test#2  for Clustering")
    test2_dict = {"a": [1, 2, 3], "b": [90, 9, 9], "c": [1, 1, 3],
                  "d": [90, 8, 8]}
    print(test2_dict)

    print(cluster.generate_clusters(test1_dict))
