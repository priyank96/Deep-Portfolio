from scipy import spatial
import networkx as nx
import community

class Cluster: 
    def generate_clusters(to_cluster):

        instruments = list(to_cluster.keys())
        similarity_measure = dict()
        for i in range(0, len(instruments)-1):
            for j in range(i+1, len(instruments)):
                similarity_measures[[instruments[i], instruments[j]]] = 1 - spatial.distance.cosine(to_cluster[instruments[i]], to_cluster[instruments[j]])

        G = nx.Graph()
        G.add_nodes_from(instruments)

        for edge in similarity_measures.keys():
            edge_tuple = list(edge)
            edge_tuple.append({'weight' : similarity_measure(edge)})
            G.add_edge(tuple(edge_tuple))

        communities = community.best_partition(G)

