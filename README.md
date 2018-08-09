# Graph Sampling Package

Graph sampling is a technique to pick a subset of vertices or edges from original graph. In some scenarios, the whole graph is known and the purpose of sampling is to obtain a smaller graph. In other scenarios, the graph is unknown and sampling is regarded as a way to explore the graph. The biggest advantage of sampling methods are their execution efficiency so that the graph transformation procedure won’t take longer time than straightforward computation on original graph. This is a simple sampling repo that helps you find a representative sample of the original graph via different sampling techniques. 

### Graph Sampling Techniques
Sampling large graphs can be done by the following exploration techniques:
  - **Simple Random Walk Sampling (SRW) :** Uniformly at random pick a starting node and then simulate a random walk on the graph.
   
    ```sh 
    random_walk_sampling_simple(complete_graph, nodes_to_sample)
    ```
  - **Random Walk Sampling with Fly Back Probability (RWF) :** Uniformly at random pick a starting node and then simulate a random walk on the graph. At every step with probability 'p' (user value) we fly back to the initial node.
    ```sh 
    random_walk_sampling_with_fly_back(complete_graph, nodes_to_sample, fly_back_prob)
    ```
  - **Induced Subgraph Random Walk Sampling (ISRW) :** Sample nodes by random walk sampling and then applied induction step to add additional edges.
     ```sh 
    random_walk_induced_graph_sampling(complete_graph, nodes_to_sample)
     ```
  - **Snowball Sampling (SB) :** Snowball Sampling is a variant of Breadth First Search where we can limit the number of neighbors k that are added to the sample. We begin from a random set of nodes of size k. After that each of the new k nodes are added that make the second sampling stage. This continues until the size is reached.
     ```sh 
    snowball(complete_graph, nodes_to_sample, k) 
     ```
  - **ForestFire Sampling (FF) :** Randomly pick a seed node and begin “burning” outgoing links and the corresponding nodes. If a link gets burned, the node at the other endpoint gets a chance to burn its own links, and so on recursively.
   ```sh 
   forestfire(complete_graph, nodes_to_sample) 
  ```
  - **Metropolis Hastings Random Walk Sampling (MHRW) :** This is very similar to random walk sampling except for the fact that we randomly select a node in graph with probability 'p'.
   ```sh  
   mhrw(complete_graph, nodes_to_sample, nodes) 
   ```
   - **Induced Metropolis Hastings Random Walk Sampling (Induced-MHRW) :** This is the improvement in MHRW sampling by appling induction step to add additional edges.
  ```sh  
   induced_mhrw(complete_graph, nodes_to_sample, nodes) 
   ```
   - **Total Induction Edge Sampling (TIES) :** In our approach, we select nodes in pairs by sampling edges in the same manner as the classic edge sampling approach. The key difference between our approach and normal edge sampling is in the induced graph step; we augment the edges selected by the edge sampling step by including other edges between the set of sampled nodes.
  ```sh 
   ties(complete_graph, nodes_to_sample, phi)
  ```
  
  

### Pre-requisite
The Sampling package requires [Python](https://www.python.org/downloads/) 2.7, 3.4, 3.5, 3.6 or newer. If you don't have the pre-installed python in your system, please follow up the python link to download it. This package also requires [Networkx](https://networkx.github.io/documentation/latest/install.html) 2.1 or newer which helps to create the graphs and also perform manipulations on them.

### Installing the development version
If you have Git installed on your system, then it is also possible to install the development version of Sampling package by running these commands on your terminal:
```sh
$ git clone https://github.com/Ashish7129/Sampling.git
$ cd Sampling
$ pip install -e .
```
Or you can install the current release of Sampling package with pip. Please
download the zip file and locate it into the current folder and then run the following command for installing the sampling package into your system:
```sh
$ pip install Sampling
```

### Usage

After installing the package, you can use the package by writing the following command:
```sh
>>> import Sampling 
```
### Example
Check out the file test.py, which helps you to understand the procedure of executing different functions along with their type and number of arguments. For example, snowball sampling fuction is excecuted as follows:
```sh
>>> object = Sampling.Snowball()             
>>> sampled_graph = object.snowball(G,size,k) 
```
*The object is the instance of the class Snowball. The class having the snowball function has 3 parameters as*
  - G : Original Graph / Whole Graph, 
  - size: number of nodes to sample and 
  - k: initial set of k nodes.


