import sampling 
import networkx as nx



g = nx.read_edgelist("fb.txt", create_using= nx.Graph(),nodetype=int)



# make an object and call function SRW
object1=sampling.SRW_RWF()


sample1 = object1.random_walk_sampling_simple(g,100) # graph, number of nodes to sample
print("Number of nodes sampled=",len(sample1.nodes()))
print("Number of edges sampled=",len(sample1.edges()))

# make an object and call function RWF
object2=sampling.SRW_RWF()
sample2= object2.random_walk_sampling_with_fly_back(g,110,0.2)  # graph, number of nodes to sample, fly-back prob
print("Number of nodes sampled=",len(sample2.nodes()))
print("Number of edges sampled=",len(sample2.edges()))

object3=sampling.Snowball()
sample3 = object3.snowball(g,28000,25) # graph, number of nodes to sample
print("Number of nodes sampled=",len(sample3.nodes()))
print("Number of edges sampled=",len(sample3.edges()))

object4=sampling.ForestFire()
sample4 = object4.forestfire(g,28000) # graph, number of nodes to sample
print("Number of nodes sampled=",len(sample4.nodes()))
print("Number of edges sampled=",len(sample4.edges()))

object5=sampling.MHRW()
sample5 = object5.mhrw(g,28000,30) # graph, number of nodes to sample
print("Number of nodes sampled=",len(sample5.nodes()))
print("Number of edges sampled=",len(sample5.edges()))

object6=sampling.TIES()
sample6 = object6.ties(g,10,0.01) # graph, number of nodes to sample
print("Number of nodes sampled=",len(sample6.nodes()))
print("Number of edges sampled=",len(sample6.edges()))
