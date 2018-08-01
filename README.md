# Sampling Package

This is a simple sampling package which helps you find a representative sample of the original graph. This can be achieved by the following exploration techniques:
  - Simple Random Walk Sampling (SRW)
  - Random Walk with Fly Back Probability (RWF)
  - Snowball Sampling (SB)
  - ForestFire Sampling (FF)
  - Metropolis Hastings Random Walk (MHRW)
  - Induced Metropolis Hastings Random Walk (Induced-MHRW) 
  - Total Induction Edge Sampling (TIES)
  
### Pre-requisite
The Sampling package requires [Python](https://www.python.org/downloads/) 2.7,3.4,3.5,3.6. If you don't have the pre-installed python in your system, please follow up the python link to download it. This package also requires [Networkx](https://networkx.github.io/documentation/latest/install.html) 2.1 or newer which helps to create the graphs and also perform manipulations on them.

### Install the development version
If you have Git installed on your system, it is also possible to install the development version of Sampling package.

Then do:
```sh
$ git clone https://github.com/Ashish7129/Sampling.git
$ cd Sampling
$ pip install -e .
```
Or you can install the current release of Sampling with pip
Download the zip file and locate it into the current folder and then run the following command for installing the sampling package into your system.
```sh
$ pip install sampling
```

### Usage

After installing the package, you can use the package by writing the following command.
```sh
>>> import sampling 
```
### test.py
Check out the file test.py, which helps you to understand the procedure of executing different functions along with there type and number of arguments. For example, snowball sampling fuction is excecuted as follows,
```sh
>>> object = sampling.Snowball()             
>>> sampled_graph = object.snowball(G,size,k) 
```
*object is the instance of the class Snowball. Class having the snowball function have 3 parameters as
G : Original Graph / Whole Graph, size: number of nodes to sample, k: initial set of k nodes*

