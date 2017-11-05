# SHARED CONSTANTS AND FUNCTIONS
# you should expect to add extra content to this file. Copy it between
# problems as you progress between them; we will mark the content of
# header.py for the last problem you solve, so make sure that file
# contains any extra content you have added

DIRECTIONS = (UP, RIGHT, DOWN, LEFT) = (0, 1, 2, 3)

def get_entry_point(maze):

    for ind_tple in range(0,len(maze[0])):
        if maze[0][ind_tple][UP]:
            return (0,ind_tple)

def get_exit_point(maze):

      for ind_tple in range(0,len(maze[-1])):
        if maze[-1][ind_tple][DOWN]:
            return (maze.index(maze[-1]),ind_tple)

# Function that can check basic things when the maze
# is of lenght 1 or more

def check_basics(maze):

    count_entry_point = 0
    count_exit_point = 0
    length = len(maze[0])

    # Checks if every row in the maze is of the same lenght

    for lst in maze:
        if len(lst)  != length:
            return False

    # Checks if there is a unique entry point in the maze and
    # if that point is at least connected to another cell

    for tple in maze[0]:
        if tple[UP]:
            false_count = 0
            count_entry_point +=1
            for direction in LEFT,DOWN,RIGHT:
                if not tple[direction]:
                    false_count += 1
            if false_count == 3:
                return False
    if count_entry_point != 1:
        return False

    # Checks if there is a unique exit point in the maze and
    # if that point is at least connected to one more cell

    for tple in maze[-1]:
        if tple[DOWN]:
            false_count = 0
            count_exit_point +=1
            for direction in LEFT,UP,RIGHT:
                if not tple[direction]:
                    false_count += 1
            if false_count == 3:
                return False
    if count_exit_point != 1:
        return False

    # Checks in every row the left and right side of it
    # if they have a wall

    for lst in maze:
        if lst[0][LEFT] or lst[-1][RIGHT]:
            return False

    # Checks every cell in the maze if it is reachable
    # from another cell

    for lst in maze:
        for tple in lst:
            false_count = 0
            for item in tple:
                if not item:
                    false_count += 1
            if false_count == 4:
                return False

    return True




# Function that validates maze

def is_valid_maze(maze):

    # Checks if Maze is an empty list

    if not maze:
        return False

    # Checks if Maze contains only 1 row

    elif len(maze) == 1:

        # Checks if the function called returns False

        if not check_basics(maze):
            return False

        # Checks if the Booelan values associated with adjacent
        # cells are symmetrical

        for ind_tple in range(0,len(maze[0])-1):
            if maze[0][ind_tple][RIGHT] != maze[0][ind_tple+1][LEFT]:
                return False

        return True

    # Checks for every other case

    else:

        if not check_basics(maze):
            return False

        # Checks if the Boolean values associated with adjacent
        # cells, DOWN and Up, are symmetrtical, and if there is
        # at least one path that connects the rows

        for ind_lst in range(0,len(maze)-1):
            count_DOWN = 0
            for ind_tple in range(0,len(maze[0])):
              if maze[ind_lst][ind_tple][DOWN] and maze[ind_lst+1][ind_tple][UP]:
                 count_DOWN += 1
              elif maze[ind_lst][ind_tple][DOWN] != maze[ind_lst+1][ind_tple][UP]:
                  return False
            if count_DOWN == 0:
                return False

        # Checks if the Boolean values associated with adjacent
        # cells, RIGHT and LEFT, are symmetrtical.

        for ind_lst in range(0,len(maze)):
            for ind_tple in range(0,len(maze[0])-1):
                if maze[ind_lst][ind_tple][RIGHT] != maze[ind_lst][ind_tple+1][LEFT]:
                    return False

        return True
