import random
import networkx as nx
# import matplotlib.pyplot as plt
import math
# import time
# import csv
# from datetime import datetime


class TIES():
    def __init__(self):
        self.G1 = nx.Graph()

    def ties(self, G, size, phi):
        V = G.nodes()
        # Calculate number of nodes in Graph G
        Vs = []
        # Empty list Vs
        phi = round((phi * 0.01), 2)
        while (len(Vs)) <= math.floor(phi * len(V)):
        # Loops run till sample size * length of V where V is number of nodes in graph as calculated above.
            edges_sample = random.sample(G.edges(), 1)
            # Randomly samples one edge from a graph at a time
            for a1, a2 in edges_sample:
            # Nodes corresponding to sample edge are retrieved and added in Graph G1
                self.G1.add_edge(a1, a2)
                if (a1 not in Vs):
                    Vs.append(a1)
                if (a2 not in Vs):
                    Vs.append(a2)
        # Statement written just to have a check of a program

        for x in self.G1.nodes():
            neigh = (set(self.G1.nodes()) & set(list(G.neighbors(x))))
            # Check neighbours of sample node and if the nodes are their in sampled set then edge is included between them.
            for y in neigh:
            # Check for every node's neighbour in sample set of nodes
                self.G1.add_edge(x, y)
                # Add edge between the sampled nodes
        return self.G1
