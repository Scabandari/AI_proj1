import datetime
from tree_search import TreeSearch
from utils import output_text_file

ASTAR_HAMMING = 'A* & hamming distance: '
ASTAR_MANHATTAN = 'A* & manhattan distance: '
ITERATIVE_DEEPENING = 'Iterative deepening: '
BFS_HAMMING = 'Best first search & hamming distance: '
BFS_MANHATTAN = 'Best first search & manhattan distance'
algo_runtimes = {}

# Get input from the user
# cols = input("Enter the number of columns: ")
# rows = input("Enter the number of rows: ")
# cols, rows = int(cols), int(rows)
# starting_list = []
# goal_state = []
# for i in range(cols*rows):
#     next_num = input("Enter the next number for the goal state: ")
#     next_num = int(next_num)
#     goal_state.append(next_num)
#
# for j in range(cols*rows):
#     next_num = input("Enter the next number for the starting list: ")
#     next_num = int(next_num)
#     starting_list.append(next_num)


# below is just for testing
cols = 4
rows = 3
# starting_list = [11, 9, 3, 7,
#                  0, 2, 6, 4,
#                  10, 1, 5, 8]
starting_list = [1, 0, 3, 7,
                 5, 2, 6, 4,
                 9, 10, 11, 8]
goal_state = [1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11, 0]

ts = TreeSearch(goal_state, cols, rows, starting_list)

# Depth first search does not find a solution on it's own
# it does however with iterative deepening
# #sol_node = ts.depth_first_search()

# A star algo & hamming
start = datetime.datetime.now()  # https://stackoverflow.com/questions/766335/python-speed-testing-time-difference-milliseconds
sol_node = ts.astar_algo(200, ts.hamming_distance)
end = datetime.datetime.now()
difference = end - start
algo_runtimes[ASTAR_HAMMING] = difference.microseconds/1000
if sol_node:
    solution_path = ts.unravel_solution(sol_node)
    print("Solution for A* algorithm using hamming distance: \n")
    ts.print_solution_boards()
    output_text_file(solution_path, "puzzleAS-h1")
    ts.reset_solution()
else:
    print("Solution not found for A* & hamming distance")

# A star algo & manhattan
# start = datetime.datetime.now()
# sol_node = ts.astar_algo(200, ts.manhattan_distance)
# end = datetime.datetime.now()
# difference = end - start
# algo_runtimes[ASTAR_MANHATTAN] = difference.microseconds/1000
# if sol_node:
#     solution_path = ts.unravel_solution(sol_node)
#     print("Solution for A* algorithm: Manhattan Distance \n")
#     ts.print_solution_boards()
#     output_text_file(solution_path, "puzzleAS-h2")
#     ts.reset_solution()
# else:
#     print("Solution not found for A* & manhattan distance")


"""For iterative deepening, may not find solution & return None
    therefore: if sol_node = it_deep()"""
# sol_node = ts.depth_first_search(15)

# iterative deepening
# start = datetime.datetime.now()
# sol_node = ts.iterative_deepening(100)
# end = datetime.datetime.now()
# difference = end - start
# algo_runtimes[ITERATIVE_DEEPENING] = difference.microseconds/1000
# if sol_node:
#     solution_path = ts.unravel_solution(sol_node)
#     print("Solution for iterative deepening: \n")
#     ts.print_solution_boards()
#     output_text_file(solution_path, "puzzleDFS")
#     ts.reset_solution()
# else:
#     print("\nSolution not found for Iterative deepening\n")

# todo don't forget to reset the solution
ts.reset_solution()
sol_node = ts.best_first_search(1000, 3)  # depth, heuristic nbr
print("Found solution using BFS manhattan distance")
sol_node.print_node()
solution_path = ts.unravel_solution(sol_node)
ts.print_solution_boards()
output_text_file(solution_path, "puzzleBFS")


print("\nThe run times for the different algorithms in millis: \n")
for algo in algo_runtimes:
    print("{}: {}".format(algo, algo_runtimes[algo]))

