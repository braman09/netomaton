### Totalistic Cellular Automata

The number of states, or colors, that a cell in a cellular automaton can adopt is given by _k_. For example, in a binary cellular automaton a cell can
assume only values of 0 and 1, and thus has _k_ = 2. A built-in function, `totalistic_ca`,
is an implementation of the [Totalistic cellular automaton rule](http://mathworld.wolfram.com/TotalisticCellularAutomaton.html),
as described in [Wolfram's NKS](https://www.wolframscience.com/nks/). The code snippet below illustrates using this rule.
A value of _k_ of 3 is used, but any value between (and including) 2 and 36 is currently supported. The rule number is
given in base 10 but is interpreted as the rule in base _k_ (thus rule 777 corresponds to '1001210' when _k_ = 3).

```python
from netomaton import *

adjacencies = AdjacencyMatrix.cellular_automaton(n=200)

initial_conditions = [0]*100 + [1] + [0]*99

activities, connectivities = evolve(adjacencies, initial_conditions, n_steps=100,
                                    activity_rule=lambda n, c, t: ActivityRule.totalistic_ca(n, k=3, rule=777))

plot_grid(activities)
```

<img src="https://raw.githubusercontent.com/lantunes/netomaton/master/resources/tot3_rule777.png" width="50%"/>