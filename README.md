Netomaton
=========

Netomaton is a Python framework for exploring discrete dynamical network
systems, also known as Network Automata. It is a software abstraction
meant to aid in the implementation of models of collective computation.

This library proposes the idea that many popular and well-known
collective computational models can all be thought of as Network Automata.
Such models include Cellular Automata, Boltzmann Machines, and various
flavours of Neural Networks, such as the Hopfield Net, and the Multilayer
Perceptron. This library does not attempt to be a replacement for great
frameworks such as TensorFlow, which are optimized, both in software and
hardware, for working with Neural Networks, for example. What this library
does attempt to be is a generalization of collective computation,
instantiated in software, with the goal of helping us see similarities
between models, and imagine new models that borrow features from existing
examples. It aims to provide a software architecture for understanding
and exploring the nature of computation in potentially dynamic networks.

### What are Network Automata?

A Network Automaton is a discrete dynamical system comprised of a collection
of cells (the computational units) causally connected to eachother, as
specified by a network-defining adjacency matrix. The cells adopt states
at each timestep of the network's evolution, as prescribed by an activity
function, *f*. Moreover, the network's topology can also change over time, as
prescribed by a connectivity function, *g*.

The network's topology is specified by the adjacency matrix, **A**, which
is of size _N_<sub>tot</sub> *X* _N_<sub>tot</sub>, where _N_<sub>tot</sub>
represents the total number of nodes (i.e. cells) in the network. Each
non-zero entry in **A** represents the existence of a link. The value of
the entry represents a weight. The matrix **A** contains information about
the existence of links, and their direction.

The network is evolved for *T* timeteps. The activity of the network is
defined by the activities of all its nodes, and is represented by **S**<sub>*t*</sub>,
where *t* is a particular timestep. During each timestep, the activity
function *f* is invoked, followed by the connectivity function *g*, such
that:

**S**<sub>*t+1*</sub> = *f*(**A**<sub>*t*</sub>, **S**<sub>*t*</sub>)

**A**<sub>*t+1*</sub> = *g*(**A**<sub>*t*</sub>, **S**<sub>*t*</sub>)


A network may have nodes added or removed at any given timestep, however,
this framework will consider that a network has a total fixed number of
nodes at all times, and that nodes may become connected or fully
disconnected from the network instead.

### Examples

This repository contains examples of implementations of
various kinds of collective computation models, all implemented using
the Netomaton framework. Follow the link to learn more:

* [Elementary Cellular Automata](https://github.com/lantunes/netomaton/blob/master/demos/elementary_ca/README.md)

* [1D Cellular Automata with Totalistic Rules](https://github.com/lantunes/netomaton/blob/master/demos/totalistic_ca/README.md)

* [Reversible 1D Cellular Automata](https://github.com/lantunes/netomaton/blob/master/demos/reversible_ca/README.md)

* [Density Classification with Evolved 1D Cellular Automata](https://github.com/lantunes/netomaton/blob/master/demos/ca_density_classification/README.md)

* [Density Classification with a Watts-Strogatz small-world graph](https://github.com/lantunes/netomaton/blob/master/demos/small_world_density_classification/README.md)

* [Asynchronous Automata](https://github.com/lantunes/netomaton/blob/master/demos/asynchronous_automata/README.md)

* [Continuous Automata](https://github.com/lantunes/netomaton/blob/master/demos/continuous_automata/README.md)

* [Langton's Lambda and Measures of Complexity](https://github.com/lantunes/netomaton/blob/master/demos/langtons_lambda/README.md)

* [2D Cellular Automata](https://github.com/lantunes/netomaton/blob/master/demos/totalistic_ca2d/README.md)

* [Conway's Game of Life](https://github.com/lantunes/netomaton/blob/master/demos/game_of_life/README.md)

* [Hopfield Network](https://github.com/lantunes/netomaton/blob/master/demos/hopfield_net/README.md)

### About this project

Netomaton arose from a personal need to reconcile various models of collective
computation. In what fundamental ways does a neural network differ from a
cellular automaton? What can a Boltmann Machine do that other models can't?
These are the questions that this library aspires to help answer.

Netomaton tries to make accessible any model of collective computation.
In so doing, it adopts certain generalizations and abstractions that,
while providing a common language for discussing disparate kinds of
models, incur a cost in terms of increased runtime complexity. The cost
of being very general is less than ideal runtime performance, as any
given implementation is not optimized for a specific setting. For
example, regarding neural networks roughly as a series of matrix
multiplications allows one to take advantage of software and hardware
that can do those operations quickly. The focus of Netomaton is not on
practicality, but on flexibility.
