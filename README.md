# Edmonds' Blossom Algorithm
## About
This is a python implementation of Edmonds' Blossom Algorithm to find a maximal-cardinality matching in a given simple graph. This was a programming exercise on the module 'Discrete Optimization (ADM II)' held by Prof. Dr. Martin Skutella at TU Berlin in summer semester 2020. I did this project together with a partner. We did this project using the pair programming paradigm, where i mainly think about the implementation and the debugging while my partner mostly think about the mathematical interpretation. Even though the running time is not guaranteed to be optimal, the code's correctness has been verified by the teaching assistant. The implementation is based on “Maximum Matchings.” Combinatorial Optimization, by Bernhard Korte and Jens Vygen, 2nd ed., Springer, 2002, pp. 219–225.

## Short Description
The program receives a graph as an input. It outputs the biggest possible matching size and a certificate verifying its optimality. The certificate is a node set <a href="https://www.codecogs.com/eqnedit.php?latex=X&space;\subseteq&space;V" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X&space;\subseteq&space;V" title="X \subseteq V" /></a> such that <br>
<a href="https://www.codecogs.com/eqnedit.php?latex=|M|&space;=&space;\frac{1}{2}(|V|-(q_G(X)-&space;|X|))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|M|&space;=&space;\frac{1}{2}(|V|-(q_G(X)-&space;|X|))" title="|M| = \frac{1}{2}(|V|-(q_G(X)- |X|))" /></a>.


## Input and Output
**INPUT**: The input is a text file. All empty lines starting with # are considered as comments and will be ignored. White spaces are ignored as well. The first two non-comment lines are: 

    n: |V|
    m: |E|
 
where V denotes the node set and E denotes the edge set. Therefore these information tell us how many nodes and edges are there. Each node and edge will get a number as their identification label. Next, for each <a href="https://www.codecogs.com/eqnedit.php?latex=v&space;\in&space;\{1,\dots,V\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v&space;\in&space;\{1,\dots,V\}" title="v \in \{1,\dots,V\}" /></a> in an arbitrary order there is a line with the form
 
<a href="https://www.codecogs.com/eqnedit.php?latex=v:&space;e_1,\dots,e_d" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v:&space;e_1,\dots,e_d" title="v: e_1,\dots,e_d" /></a> 

where <a href="https://www.codecogs.com/eqnedit.php?latex=e_1,\dots,e_d&space;\in&space;\{1,\dots,|E|\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_1,\dots,e_d&space;\in&space;\{1,\dots,|E|\}" title="e_1,\dots,e_d \in \{1,\dots,|E|\}" /></a>  are the numbers of the edges that are incident to node <a href="https://www.codecogs.com/eqnedit.php?latex=v" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v" title="v" /></a>.

<br>

**OUTPUT**: The output is a text file. It has two non-comment lines of the form

<a href="https://www.codecogs.com/eqnedit.php?latex=M:&space;e_1,\dots,e_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?M:&space;e_1,\dots,e_k" title="M: e_1,\dots,e_k" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=X:&space;v_1,\dots,v_{\ell}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X:&space;v_1,\dots,v_{\ell}" title="X: v_1,\dots,v_{\ell}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=e_1,\dots,e_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_1,\dots,e_k" title="e_1,\dots,e_k" /></a> are the numbers of the matching edges and <a href="https://www.codecogs.com/eqnedit.php?latex=v_1,\dots,v_{\ell}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_1,\dots,v_{\ell}" title="v_1,\dots,v_{\ell}" /></a> are the numbers of the nodes that belong in the node set certifying optimality of the matching.

## How to Use   
1. If you use Linux/MacOS, open terminal. If you use windows, use e.g. [Ubuntu terminal](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab)
2. Go to the location of the program `edmonds.py`
3. Once you're in the directory, type the following:

        edmonds.py <input file name> <output file name>

4.  The output file with the desired name is now created in the directory

