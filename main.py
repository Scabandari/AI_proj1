from tree_search import TreeSearch
from utils import output_text_file
import heapq as heap

# Get input from the user
# cols = input("Enter the number of columns: ")
# rows = input("Enter the number of rows: ")
# cols, rows = int(cols), int(rows)
# starting_list = []
# for i in range(cols*rows):
#     next_num = input("Enter the next number: ")
#     next_num = int(next_num)
#     starting_list.append(next_num)


# below is just for testing
cols = 4
rows = 3
starting_list = [11, 9, 3, 7,
                 0, 2, 6, 4,
                 10, 1, 5, 8]
goal_state = [1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11,  0]

""""For h1 and h2 for best first search see notes on search around slide 70"""
ts = TreeSearch(goal_state, cols, rows, starting_list)

# #sol_node = ts.depth_first_search()
# sol_node = ts.astar_algo()
# solution_path = ts.unravel_solution(sol_node)
# ts.print_solution_boards()
# #output_text_file(solution_path, "puzzleDFS")
# output_text_file(solution_path, "puzzleAS-h1")

sol_node = ts.depth_first_search(15)
# sol_node = ts.best_first_search(1000, 3)  # depth, heuristic nbr
# sol_node.print_node()
solution_path = ts.unravel_solution(sol_node)
ts.print_solution_boards()
#output_text_file(solution_path, "puzzleDFS")
output_text_file(solution_path, "puzzleAS-h1")

