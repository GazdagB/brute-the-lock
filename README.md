# Brute The Lock

Brute The Lock by Gazdag is an educational Python simulator for visualizing how Android-style 3x3 pattern combinations can be generated and tested.

The goal is not to bypass real devices, but to understand:

- graph traversal
- backtracking
- brute-force search
- pattern validation
- GUI visualization

## Grid Numbering

```text
1 2 3
4 5 6
7 8 9
```

## The middle Dots 
A better way to actually know where can we step and where not or if a move is valid or not is by stroin the required 
middle dots between the numbered dots. 


```Python 
REQUIRED_MIDDLE_DOT = {
    (1, 3): 2,
    (3, 1): 2,
    (1, 7): 4,
    (7, 1): 4,
    (3, 9): 6,
    (9, 3): 6,
    (7, 9): 8,
    (9, 7): 8,
    (1, 9): 5,
    (9, 1): 5,
    (3, 7): 5,
    (7, 3): 5,
    (2, 8): 5,
    (8, 2): 5,
    (4, 6): 5,
    (6, 4): 5,
}
```
