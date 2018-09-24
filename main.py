from board import Board
from tree_search import TreeSearch

""""For h1 and h2 for best first search see notes on search around slide 70"""
goal_state = [1, 2, 3, 4, 5, 0]

cols = 3
rows = 2
initial_state = [3, 0, 4, 2, 5, 1]

ts = TreeSearch(goal_state, cols, rows, initial_state)

sol_node = ts.depth_first_search()
sol_node.print_node()

# def swap(state, zero_index, swap_index):
#     swap_holder = state[zero_index]
#     state[zero_index] = state[swap_index]
#     state[swap_index] = swap_holder
#     return state
#
#
# state = [1, 2, 0, 3]
# while state:
#     print(state.pop(0))
