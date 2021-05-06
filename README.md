# GameForSAS
This is the public version of our paper:

Component Level Game-Based Self-Adaptation for Secure Industrial Control System

## Requirements

We use networkx to establish a component graph,
and use gambit Python API to solve the game tree.

networkx

gambit (http://www.gambit-project.org/)

pandas

numpy



## run the game generator:
```
python generate_tree.py
```

## solve the game
```
python compute_equilibrium.py
```

## results:
![figure](rq-test.png)

