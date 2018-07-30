import random
import time
import networkx as nx
import matplotlib.pyplot as plt

class MHRW():
    def __init__(self):
        self.G1 = nx.Graph()

    def mhrw(self,G, size, node):
        random_nodes = set()
        dictt = set()
        random_nodes.update(list(G.neighbors(node)))
        #print(random_nodes)
        deg_v = G.degree(node)
        #print(deg_v)
        z = node
        dictt.add(z)
        while(len(self.G1.nodes()) <= size):
            z=node  
            if(len(random_nodes)>0):
                random_nodes.update(G.neighbors(z))
                #print(random_nodes)
                deg_p = G.degree(z)
                w = random_nodes.pop()
                if(w not in dictt):
                    dictt.add(w)
                    deg_c = G.degree(w)
                    p = round(random.uniform(0,1),4)
                    if(p <= min(1,deg_p/deg_c)):
                        self.G1.add_edge(z,w)
                        z = w
                        random_nodes.clear()
                    else:
                        dictt.remove(w)
            else:
                print len(self.G1.nodes())
                node = random.sample(G.nodes(),1)
                random_nodes.clear()
                
        return self.G1
