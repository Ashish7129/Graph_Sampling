import sampling 
import random
import time
import datetime
import io
import array,re,itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import groupby

def create_graph_edge_list(path,name):
        g = nx.read_edgelist(path, create_using= nx.Graph(),nodetype=int)
        g = nx.convert_node_labels_to_integers(g, 0, 'default', True)
        print name+" Graph created."
        #giving unique id to every node same as built-in function id
        for n, data in g.nodes(data=True):
            g.node[n]['id']= n
        return g


#g1 = create_graph_edge_list("fb.txt","Facebook")

g = nx.read_edgelist("fb.txt", create_using= nx.Graph(),nodetype=int)
print "done"
# make an object and call function SRW
object1=sampling.SRW_RWF()
#sample1 = object1.random_walk_sampling_simple(g1,100) # graph, number of nodes to sample
#print "Number of nodes sampled=",len(sample1.nodes())

# make an object and call function RWF
object2=sampling.SRW_RWF()
#sample2= object2.random_walk_sampling_with_fly_back(g1,110,0.2)  # graph, number of nodes to sample, fly-back prob
#print "Number of nodes sampled=",len(sample2.nodes())

# object3=sampling.Snowball()
# sample3 = object3.snowball(g,28000,25) # graph, number of nodes to sample
# print "Number of nodes sampled=",len(sample3.nodes())
# print "Number of edges sampled=",len(sample3.edges())

# object4=sampling.ForestFire()
# sample4 = object4.forestfire(g,28000) # graph, number of nodes to sample
# print "Number of nodes sampled=",len(sample4.nodes())
# print "Number of edges sampled=",len(sample4.edges())

# object4=sampling.MHRW()
# sample4 = object4.mhrw(g,28000,30) # graph, number of nodes to sample
# print "Number of nodes sampled=",len(sample4.nodes())
# print "Number of edges sampled=",len(sample4.edges())

object4=sampling.TIES()
sample4 = object4.ties(g,10,0.01) # graph, number of nodes to sample
print "Number of nodes sampled=",len(sample4.nodes())
print "Number of edges sampled=",len(sample4.edges())
