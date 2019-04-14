import Graph_Sampling 
import networkx as nx

# read facebook network edge list "fb.txt" and return a graph g. 
g = nx.read_edgelist("fb.txt", create_using= nx.Graph(),nodetype=int)

# make an object and call function SRW
object1=Graph_Sampling.SRW_RWF_ISRW()
sample1 = object1.random_walk_sampling_simple(g,100) # graph, number of nodes to sample
print("Simple Random Walk Sampling:")
print("Number of nodes sampled=",len(sample1.nodes()))
print("Number of edges sampled=",len(sample1.edges()))

# make an object and call function RWF
object2=Graph_Sampling.SRW_RWF_ISRW()
sample2= object2.random_walk_sampling_with_fly_back(g,110,0.2)  # graph, number of nodes to sample, fly-back probability
print("Random Walk Sampling with flyback:")
print("Number of nodes sampled=",len(sample2.nodes()))
print("Number of edges sampled=",len(sample2.edges()))

# make an object and call function ISRW
object3=Graph_Sampling.SRW_RWF_ISRW()
sample3= object3.random_walk_induced_graph_sampling(g,120)  # graph, number of nodes to sample
print("Induced Subgraph Random Walk Sampling:")
print ("Number of nodes sampled=",len(sample3.nodes()))
print ("Number of edges sampled=",len(sample3.edges()))

# make an object and call function SB
object3=Graph_Sampling.Snowball()
sample3 = object3.snowball(g,28000,25) # graph, number of nodes to sample , k set
print("Snowball Sampling:")
print("Number of nodes sampled=",len(sample3.nodes()))
print("Number of edges sampled=",len(sample3.edges()))

# make an object and call function FF
object4=Graph_Sampling.ForestFire()
sample4 = object4.forestfire(g,28000) # graph, number of nodes to sample
print("Forest Fire Sampling")
print("Number of nodes sampled=",len(sample4.nodes()))
print("Number of edges sampled=",len(sample4.edges()))

# make an object and call function MHRW
object5=Graph_Sampling.MHRW()
sample5 = object5.mhrw(g,28000,30) # graph, number of nodes to sample, initial seed node
print("Metropolis Hasting Random Walk Sampling:")
print("Number of nodes sampled=",len(sample5.nodes()))
print("Number of edges sampled=",len(sample5.edges()))

# make an object and call function TIES
object6=Graph_Sampling.TIES()
sample6 = object6.ties(g,10,0.01) # graph, number of nodes to sample, phi
print("TIES:")
print("Number of nodes sampled=",len(sample6.nodes()))
print("Number of edges sampled=",len(sample6.edges()))
