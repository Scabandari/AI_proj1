

class Node(object):

    def __init__(self, depth, board, action=None, parent_node=None):
        self.parent_node = parent_node
        self.board = board
        self.depth = depth
        self.action = action
        #self.zero_index = zero_index

    def make_move(self, move):
        """This function passes the move to be made to the Board class"""
        pass

    def print_node(self):
        if self.parent_node is None:
            print("0 ", self.board.state)
        else:
            print(self.action, self.board.state)











