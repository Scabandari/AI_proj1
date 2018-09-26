from node import Node
from board import Board
from copy import deepcopy


class TreeSearch(object):

    def __init__(self, board_cols, board_rows, starting_list):
        # self.correct_state = [1, 2, 3, 0]
        self.correct_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,  0]
        self.board_cols = board_cols
        self.root_node = Node(
            depth=0,
            #board=Board(2, 2, [3, 0, 1, 2])
            board=Board(board_cols, board_rows, starting_list)
        )
        self.open = [self.root_node]
        self.closed = []
        self.board_moves = {
            1: Board.UP,
            2: Board.UP_RIGHT,
            3: Board.RIGHT,
            4: Board.DOWN_RIGHT,
            5: Board.DOWN,
            6: Board.DOWN_LEFT,
            7: Board.LEFT,
            8: Board.UP_LEFT
        }
        self.solution = []

    def check_goal_state(self, node):
        for piece, index in enumerate(node.board.state):
            if self.correct_state[index] != node.board.state[index]:
                return False
        return True

    def depth_first_search(self):
        pass
        while self.open:
            visit_node = self.open.pop(0)
            if self.check_goal_state(visit_node):
                sol_node = deepcopy(visit_node)

                return visit_node

            children = self.generate_children(visit_node.depth, visit_node)
            # add children to open, depth first --> LIFO

            while children:
                node = children.pop(0)
                self.open.append(node)
            self.closed.append(visit_node)

    def generate_children(self, parent_depth, parent_node):
        """This function should generate all possible moves except for the move
        that would undo the move that got to this current state: action"""
        # child states should not equal parent_state

        # take the parent node and generate all possible children
        children = []
        for key, value in self.board_moves.items():
            new_state, letter_move = parent_node.board.make_move(value)
            if new_state:
                new_board = Board(parent_node.board.cols, parent_node.board.rows, new_state)
                new_node = Node(parent_depth + 1, new_board, action=letter_move, parent_node=parent_node)
                if self.check_children(new_node, parent_node):
                    children.append(new_node)
        return children

    def check_children(self, child_node, parent_node):
        """When generating children nodes we have to check if nodes w/ the same 'state' are
            already in either lists open or closed. Also children's state should not be the
            same as the parents state ie we don't want to back a move. Returns True if
            Node is truly new and therefor useful"""
        if TreeSearch.same_state(child_node, parent_node):
            return False
        for node in self.open:
            if TreeSearch.same_state(node, child_node):
                return False
        for node in self.closed:
            if TreeSearch.same_state(node, child_node):
                return False
        return True

    @staticmethod
    def same_state(node_1, node_2):
        """Checks if state_1 and state_2 are equal"""
        for i in range(len(node_1.board.state)):
            if not node_1.board.state[i] == node_2.board.state[i]:
                return False
        return True

    def unravel_solution(self, sol_node):
        """This function should recursively add solution nodes board and move info to
        self.solution so we can display it or add it to solution text files """
        if sol_node.parent_node is None:
            self.solution.insert(0, (0, deepcopy(sol_node)))
            return self.solution

        self.solution.insert(0, (deepcopy(sol_node.action), deepcopy(sol_node)))
        self.unravel_solution(sol_node.parent_node)
        return self.solution

    def reset_solution(self):
        """In case we're using self.solution with multiple different search techniques"""
        self.solution = []

    def print_solution_boards(self):
        for tuple_ in self.solution:
            tuple_[1].board.print_board()







