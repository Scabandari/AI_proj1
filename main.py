from board import Board
from tree_search import TreeSearch

""""For h1 and h2 for best first search see notes on search around slide 70"""
ts = TreeSearch()

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




