# Graph Sampling Package

[Social Network Analysis](https://en.wikipedia.org/wiki/Social_network_analysis) (SNA) has recently been gaining more and more popularity in various domains. Unfortunately, performing SNA is not always an easy task, due to the volume of data which translates to huge network/graph, it is very time consuming and [computationally expensive](https://en.wikipedia.org/wiki/Computational_complexity) to perform analysis on these graphs. Depending on the type of task, handling graphs with even just dozens of thousands of nodes can be unfeasible, as some studies show. An intuitive solution to deal with this situation, just as in any scenario where we have a massive amount of data, is to sample the graph and then perform relevant simulation/analysis on obtained [sub-graph](https://en.wikipedia.org/wiki/Subgraph).
<p> <a href="https://en.wikipedia.org/wiki/Sampling_(statistics)">Graph sampling</a> is a technique to pick a subset of vertices or edges from original graph. The biggest advantage of sampling methods are their execution efficiency so that the graph transformation procedure won’t take longer time than straightforward computation on original graph. This is a simple sampling repo that helps you find a representative sample of the original graph via different <a href="https://cs.stanford.edu/~jure/pubs/sampling-kdd06.pdf">Sampling Techniques</a>.</p> 

### 1. Sampling by Exploration
Exploration or traversal (also called topology-based) approaches are based on the idea of randomly selecting one node and then exploring its neighborhood. Sampling algorithms based on this techniques are :

- **Simple Random Walk Sampling (SRW) :** Uniformly at random pick a starting node and then simulate a [random walk](https://people.math.osu.edu/husen.1/teaching/571/random_walks.pdf)(select neighboring node uniformly and randomly) on the graph. Random walk is continued until we reach the required sample size.
  <p> In the unconnected graph, it is possible that there is no node in the component that could be added to the sample. To handle this we defined a time period and an expected growth size in that period and after some iterations check whether the sample growth is large enough and if not, select again the node randomly to continue random walk. This way we ensure that the sample will reach the required size .</p>
```sh 
  sampled_graph = random_walk_sampling_simple(complete_graph, nodes_to_sample)
```

- **Random Walk Sampling with Fly Back Probability (RWF) :** In *SRW* at any stage, we choose only one of the neighboring node to continue random walk. Choosing only one neighboring node affects graph properties like average degree which in turn affect many properties related to it.
  <p> <em>RWF</em> is a variation of random walk to improve the performance. The Fly-back probability <em>(p)</em> is used to sample more than one neighboring node at any stage of already sampled node. <em>RWF</em> picks a node uniformly at random as start point and begins a sequence. At each step, with <em>1-p</em> probability it selects one node among neighbors of the current node with equal probability and moves to that node. If the neighboring node or the corresponding edge does not exist in the sample graph, they will be added to the graph; with <em>p</em> probability, we will fly back to the starting point. This ensures that the neighborhood of a selected node could be sufficiently explored. The higher the fly back probability, the more similar random walk is to <a href="https://en.wikipedia.org/wiki/Breadth-first_search">Breadth First Search</a>. </p>
  <p>To avoid being stuck we defined a time period and an expected growth size in that period and after iterations check whether the sample growth is large enough and if not, select again the node randomly to continue random walk. This way we ensure that the sample will reach the required size.</p>
```sh 
  sampled_graph = random_walk_sampling_with_fly_back(complete_graph,nodes_to_sample,p)
```
- **Induced Subgraph Random Walk Sampling (ISRW) :**  We observed that *SRW* and *RWF* fundamentally biases the structure of the sampled subgraph, as at every step we choose only one neighbor uniformly and randomly of the node we sampled at the previous iteration. When a node is selected for inclusion in the sample, it is unlikely that all of its neighbors will be included in the sampled subgraph, and thus, sampled degrees of nodes tend to be smaller than original degrees. As random walk moves in the linear fashion, the connectivity in the sampled subgraph was also quite sparse due to under-sampling of edges. This under-sampling of edges caused overestimation of shortest path lengths in sampled subgraphs. Hence, this conventional wisdom of selecting nodes in an unbiased manner (e.g., uniformly at random) may not yield representative subgraphs that match the properties of the original graph.
  <p>So, we presented our new sampling strategy, <em>Induced Subgraph Random Walk Sampling (ISRW)</em>, which tries to overcome the problem of undersampling of edges in <em>SRW</em>. We applied graph <a href="https://en.wikipedia.org/wiki/Induced_subgraph">induction</a> step to <em>SRW</em> to select additional edges between sampled nodes with the aim to restore connectivity and bring the structure closer to that of the original graph.</p>
```sh 
  sampled_graph = random_walk_induced_graph_sampling(complete_graph, nodes_to_sample)
```
- **Snowball Sampling (SB) :** Snowball Sampling is a variant of [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search) where there is limit on the number of neighbors <em>k</em> that are added to the sample. Begin from a random set of nodes of size <em>k</em>. After that each of the new <em>k</em> nodes are added that make the second sampling stage. This continues until the sample size is reached.
  <p>The Snowball sampling is a type of a sampling by exploration in which each individual in the sample is asked to name k different individuals in the population, where <em>k</em> is a specified integer; for example, each individual may be asked to name his "k colleagues". The individuals who were not in the random sample already but were named by individuals in it form the first stage. Each of the individuals in the first stage is then asked to name <em>k</em> different individuals. The individuals who were not in the random sample nor in the first stage but were named by individuals who were in the first stage form the second stage. Each of the individuals in the second stage is then asked to name <em>k</em> different individuals. The individuals who were not in the random sample nor in the first or second stages but were named by individuals who were in the second stage form the third stage. This procedure is continued until each of the individuals in the <em>d-th</em> stage has been asked to name <em>k</em> different individuals.</p>
  <p>Snowball Sampling starts with a set of nodes, say <em>k</em>. For each node, exactly <em>k</em> of it's neighbours are extracted. If the neighbours of a node is less than <em>k</em> , then all the neighbours of the node are extracted. This process continues until the required sample size is reached. In this way, a sampled graph is extracted from the original graph.</p>

```sh 
  sampled_graph = snowball(complete_graph, nodes_to_sample, k) 
```
- **ForestFire Sampling (FF) :** Randomly pick a seed node and begin “burning” outgoing links and the corresponding nodes. If a link gets burned, the node at the other endpoint gets a chance to burn its own links. This process is recursively repeated for each burnt neighbor until no new node is selected, and a new random node is chosen to start the process until we obtain the desired sample size.
```sh 
  sampled_graph = forestfire(complete_graph, nodes_to_sample) 
```
- **Metropolis Hastings Random Walk Sampling (MHRW) :** This is very similar to random walk sampling. Initially, a user selected node *v*  with non-zero degree is set as the seed. We define the proposal function as *Q(v) = k<sub>v</sub>*, which is the degree of node *v*. From node *v’s* neighbors, *MHRW* randomly chooses a node *w*, and then generates a random number *p* from uniform distribution *U(0, 1)*. If *p ≤ Q(v)/Q(w)*, the proposal is accepted and the sampling process will transit to *w*; otherwise, it stays at node *v*. MHRW stops when the budget is reached.
```sh  
  sampled_graph = mhrw(complete_graph, nodes_to_sample, initial_seed_node) 
```
- **Induced Metropolis Hastings Random Walk Sampling (Induced-MHRW) :** This is the improvement in MHRW sampling by appling [induction](https://en.wikipedia.org/wiki/Induced_subgraph) step to add additional edges.
```sh  
  sampled_graph = induced_mhrw(complete_graph, nodes_to_sample, initial_seed_node) 
```

### 2. Edge Sampling 
Edge sampling focuses on the selection of edges rather than nodes to populate the sample. Thus, the node selection step in edge sampling algorithm proceeds by just sampling edges, and including both nodes when a particular edge is sampled.
- **Total Induction Edge Sampling (TIES) :** The algorithm runs in an iterative fashion, picking an edge at random from the original graph and adding both the nodes to the sampled node set in each iteration as in the classic [edge sampling](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=2743&context=cstech) approach. It stops adding nodes once a target fraction *φ* of nodes are collected. After this, the algorithm proceeds to the graph induction step where it walks through all the edges in the graph and forms the induced graph by adding all edges which have both end-points already in the sampled node set.
```sh 
  sampled_graph = ties(complete_graph, nodes_to_sample, φ)
```
  
  
### Pre-requisite
The Graph Sampling package requires [Python](https://www.python.org/downloads/) 3.X . If you don't have the pre-installed python in your system, please follow up the python link to download it. This package also requires [Networkx](https://networkx.github.io/documentation/latest/install.html) 2.1 or newer which helps to create the graphs and also perform manipulations on them.

### Installing the development version
If you have Git installed on your system, then it is also possible to install the development version of Graph Sampling package by running these commands on your terminal:
```sh
$ git clone https://github.com/Ashish7129/Graph_Sampling.git
$ cd Graph_Sampling
$ pip install -e .
```
Or you can install the current release of Graph Sampling package with pip. Please download the zip file and locate it into the current folder and then run the following command for installing the graph sampling package into your system:
```sh
$ python setup.py sdist bdist_wheel
$ pip install dist/Graph_Sampling-0.0.1-py3-none-any.whl
```
 
### Usage

After installing the package, you can use the package by writing the following command:
```sh
>>> import Graph_Sampling 
```
### Example
Check out the file test.py, which helps you to understand the procedure of executing different functions along with their type and number of arguments. For example, snowball sampling fuction is excecuted as follows:
```sh
>>> object = Graph_Sampling.Snowball()             
>>> sampled_subgraph = object.snowball(G,size,k) 
```
*The object is the instance of the class Snowball. The class having the snowball function has 3 parameters as :*
  - G : Original Graph / Whole Graph, 
  - size: number of nodes to sample and 
  - k: initial set of k nodes.


