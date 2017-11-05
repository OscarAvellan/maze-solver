# maze-solver

Automatically determines the path through a maze.

The maze is provided in the form of a (rectangular) 2-dimensional list, with each item taking the form of a 4-tuple of Boolean values, stipulating whether it is possible to navigate up, to the right, down, and to the left, respectively of the current cell. For example: cell = (False, True, True, False)

To run it:

python -c 'import maze_solver; print maze_solver.solve_maze([[(True, True, False, False), (False, False, True, True)], [(False, True, True, False), (True, False, False, True)]])'
