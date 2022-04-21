# Pirates: Hide and Seek solver
Solver for "Pirates: Hide and Seek" game by SmartGames:

!["Pirates: Hide and Seek" by SmartGames](./pirates.png)

Written by Dmitry Baranov as a "Hello, World!" exercise to learn Python.

It uses a bruteforce approach by calculating all possible masks transpositions and permuting them between 4 positions.

It gives all possible solutions for a given challenge.

# Requirements
- Python3

# Usage
```
python3 app.py
```
or, if you want to skip interactive challenge prompt:
```
echo 5,0,0,0,0 | python3 app.py
```

Challenge should be entered as a comma-separated list of 5 integers:

- Number of "white" pirate ships
- Number of "red" pirate ships
- Number of islands
- Number of caves
- Number of boats

# Example run
```
% python3 app.py

SmartGames "Pirates: Hide and Seek" game solver by Dmitry Baranov
made as an entry "Hello, World!" application in Python
===
Format of the input: WHITE_SHIPS,RED_SHIPS,ISLANDS,CAVES,BOATS integer numbers
For example: 2,1,2,0,0

Please enter a challenge: 5,0,0,0,0

Challenge: {'W': 5, 'R': 0, 'I': 0, 'C': 0, 'B': 0}

Solved by:

▒▒▒    ▒▒
▒▒▒   ▒▒▒
 ▒▒   ▒▒

▒▒    ▒▒▒
▒▒▒   ▒ ▒
▒▒     ▒▒

```
