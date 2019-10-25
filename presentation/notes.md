// Lightning Talk @GeoDataScience

# What is Agent-Based Modelling? (1)

"An agent-based model (ABM) is a class of computational models for simulating the actions and interactions of autonomous agents with a view to assessing their effects on the system as a whole."

Combines elements of:
- game theory, 
- complex systems, 
- emergence, 
- computational sociology, 
- multi-agent systems, 
- evolutionary programming.

# What is Agent-Based Modelling? (2)

Most agent-based models are composed of: (1) numerous agents specified at various scales (typically referred to as agent-granularity); (2) decision-making heuristics; (3) learning rules or adaptive processes; (4) an interaction topology; and (5) an environment. ABMs are typically implemented as computer simulations, either as custom software, or via ABM toolkits, and this software can be then used to test how changes in individual behaviors will affect the system's emerging overall behavior.

# History of Agent-Based Modelling

"The idea of agent-based modeling was developed as a relatively simple concept in the late 1940s. Since it requires computation-intensive procedures, it did not become widespread until the 1990s."

# Early Developments (1)

## Von Neumann (1966). Theory of Self-Reproducing Automata.

Von Neumann's goal was to specify an abstract machine which, when run, would replicate itself. In his design, the machine consists of three parts: a 'blueprint' for itself, a mechanism that can read any blueprint and construct the machine (sans blueprint) specified by that blueprint, and a 'copy machine' that can make copies of any blueprint. 

# Early Developments (2)

## John Conway (1970). Game of Life

Rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

![Game of Life Visualisation](giphy.gif)

# First Models (1970s & 1980s) (1)

## Thomas Schelling (1969). Models of Segregation. 

"Some segregation is organized... some results from the interplay of individual choices that discriminate."

"...at dinner, with men and women seated alternately, everyone is outnumbered two to one locally by the opposite sex but can join a three-fifths majority if he extends his horizon to the next person on either side..."

"Imagine a line along which blacks and whites have been distributed in equal numbers and random order...
Define everybody's 'neighbourhood' as extending four neighbours on either side, and suppose that everyone is content if half his 'neighbours' are the same color as he. If fewer than half are his color, he moves in either direction to the nearest point at which half his eight nearest neighbors are the same color as he."

Simulation:
[http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/](http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/)

# First Models (1970s & 1980s) (2)

## Robert Axelrod (1984). The Evolution of Cooperation.

- Prisoner's Dilemma tournament.

- Winning strategy: TIT FOR TAT.

- Lessons:
	1. **Be nice.**
	2. **Be provocable.**
	3. **Don't be envious.**
	4. **Don't be too clever.**

# Applications

- Disease Dynamics in a Refugee Camp

- Modelling the Emergence of Riots

- Exploring the Growth of Slums

- The Spread of Agriculture during the Neolithic Period

SRC: Crooks, Malleson, et al. (2019). Agent-Based Modelling & Geographical Information Systems. pp.311-328 + links to source code.

# Critique

## Ontology
Livet, Phan & Sanders 2008, [Why do we need Ontology for Agent-Based Models](https://www.researchgate.net/publication/227112082_Why_do_we_need_Ontology_for_Agent-Based_Models)

'the question of the ontological compatibility between the “model world” and the “real world.'

## Causal Explanation
Grune-Yanoff 2008, [The explanatory potential of artificial societies](https://link.springer.com/article/10.1007%2Fs11229-008-9429-0)

'... models do *not* provide potential causal explanations. Instead... they provide potential functional explanations.'

# A Simple Example: Rabbit Population Dynamics. (1)
## Define an Environment class 

# A Simple Example: Rabbit Population Dynamics. (2)
## Define an Agent class

# A Simple Example: Rabbit Population Dynamics. (3)
## Define a Rabbit child-class

# A Simple Example: Rabbit Population Dynamics. (4)
## Run Model!

