from tree_search import TreeSearch
from utils import output_text_file

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
starting_list = [1, 0, 3, 7, 5, 2, 6, 4, 9, 10, 11, 8 ]

""""For h1 and h2 for best first search see notes on search around slide 70"""
ts = TreeSearch(cols, rows, starting_list)
sol_node = ts.depth_first_search()
solution_path = ts.unravel_solution(sol_node)
ts.print_solution_boards()
output_text_file(solution_path, "puzzleDFS")





