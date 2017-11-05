from header import UP, RIGHT, DOWN, LEFT
from header import get_entry_point, get_exit_point
from header import is_valid_maze

def solve_maze(maze):

  entry_point = get_entry_point(maze)
  exit_point = get_exit_point(maze)
  ind_lst,ind_tple = entry_point
  path = [entry_point]
  ind_path = -1
  invalid_path = []
  final_path = []

  if not is_valid_maze(maze):
    return False


  while path[-1] != exit_point:
    try:

      # Checks if it can go to the LEFT side of the cell
      # and if the next cell is not in the list

      if maze[ind_lst][ind_tple][LEFT] and (ind_lst,ind_tple-1) not in path:
          ind_tple = ind_tple-1
          path.append((ind_lst,ind_tple))

      # Checks if it can go to the DOWN side of the cell
      # and if the next cell is not in the list

      elif maze[ind_lst][ind_tple][DOWN] and (ind_lst+1,ind_tple) not in path:
          ind_lst = ind_lst+1
          path.append((ind_lst,ind_tple))

      # Checks if it can go to the RIGHT side of the cell
      # and if the next cell is not in the list

      elif maze[ind_lst][ind_tple][RIGHT] and (ind_lst,ind_tple+1) not in path:
          ind_tple = ind_tple+1
          path.append((ind_lst,ind_tple))

      # Checks if it can go to the UP side of the cell
      # and if the next cell is not in the list

      elif maze[ind_lst][ind_tple][UP] and (ind_lst-1,ind_tple) not in path:
          ind_lst = ind_lst-1
          path.append((ind_lst,ind_tple))

      # Checks if there is a dead end and goes backwards
      # in the list to find an alternative path
      else:
          # Adds the wrong path into a list
          invalid_path.append(path[ind_path])
          ind_path -= 1
          ind_lst,ind_tple = path[ind_path]

    # If there is now way to get to the exit point, an
    # IndexError will jump and it will return None
    except IndexError:
        return None

  # Appends the correct path into final_path
  for item in path:
      if item not in invalid_path:
          final_path.append(item)


  return final_path
