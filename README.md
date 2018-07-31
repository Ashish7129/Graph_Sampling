# Sampling Package

This is a simple sampling package. You can sample the original graph by using the following methods:
  - Simple Random Walk
  - Random Walk Fly Back
  - Snowball 
  - ForestFire
  - MHRW : Metropolis Hastings Random Walk
  - TIES : Total Induction Edge Sampling
  
### Pre-requisite
sampling package requires [Python](https://www.python.org/downloads/) 2.7,3.4,3.5,3.6. If you don't have the pre-installed python. Please follow up the link.Our package also requires [Networkx](https://networkx.github.io/documentation/latest/install.html) 2.1 or newer.

### Installation
Download the zip file and locate to the current folder and then run this command for installing the sampling package into your system
```sh
$ pip install sampling
```

### Usage

After installing the package. You can use the package by writing the following command.

```sh
import sampling 
```
### test.py
Check out the file test.py, which helps to understand the procedure of executing the different functions with different type of arguments.As for example, we take snowball sampling,
```sh
object = sampling.Snowball()             
sampled_graph = object.snowball(G,size,k) 
```
*object is the instance of the class Snowball. Class having the snowball function which have 3 parameters as
G : Original Graph / Whole Graph, size: number of nodes you need to sampled, k: initial set of k nodes*

