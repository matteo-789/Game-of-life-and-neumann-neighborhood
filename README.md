# Game-of-life-and-neumann-neighborhood
Scratch implementation of cellular automata with neumann neighborhood and conway's game of life rules

## Requirements

The requirements are:
        - numpy
        - pygame

## Von neumann neighborhood

Implementation of Von Neumann neighborhood with simple rules:
        - if only one cell is alive change current to alive
        - otherwise change to dead

To run the Von Neumann neighborhood with those rules use the following command:
```
python3 main.py neumann
```

## Conway's game of life

Implementation of Conway's game of life rules in black and white(black is alive and white dead).

To run the game of life use the following command:
```
python3 main.py gol -x X
```

## Help

For help use the following commands:
```
python3 main.py -h
python3 main.py gol -h
python3 main.py neumann -h
```
