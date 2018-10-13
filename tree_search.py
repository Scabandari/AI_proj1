from operator import itemgetter
from node import Node
from board import Board
from copy import deepcopy
from utils import first_two


"""
Something we can reference for tie breaking in the report here:
https://stackoverflow.com/questions/18414995/how-can-i-sort-tuples-by-reverse-yet-breaking-ties-non-reverse-python#18415016
We'll sort by the latest move of the node which is node.board.move_series[-1]
Referencing the link above we can use sorted which sorts by each element in the tuple.
Our tuples will look like (f(n), tie breaker, node) meaning sorted() will try to sort by type
node which it can't therefore key=first_two
# https://www.programiz.com/python-programming/methods/built-in/sorted

"""


class TreeSearch(object):

    def __init__(self, goal_state, board_cols, board_rows, starting_list):
        # self.correct_state = [1, 2, 3, 0]
        self.correct_state = goal_state  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,  0]
        self.board_cols = board_cols
        self.board_rows = board_rows
        self.starting_list = starting_list
        self.root_node = Node(
            depth=0,
            # board=Board(2, 2, [3, 0, 1, 2])
            board=Board(self.board_cols, self.board_rows, deepcopy(starting_list))
        )
        self.open = [deepcopy(self.root_node)]
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
        self.HEURISTIC = False

    def check_goal_state(self, node):
        for index in range(len(node.board.state)):
            if self.correct_state[index] != node.board.state[index]:
                return False
        return True

    def depth_first_search(self, depth):  # todo DFS not finding solution?
        self.HEURISTIC = False
        self.open = [self.root_node]
        self.closed = []
        while self.open:
            visit_node = self.open.pop(0)
            if self.check_goal_state(visit_node):
                return visit_node

            # visit_node.print_node()
            if visit_node.depth >= depth:
                # print("ey")
                continue
            children = self.generate_children(visit_node.depth, visit_node)
            # add children to open, depth first --> LIFO
            while children:
                node = children.pop(0)
                self.open.insert(0, node)
            self.closed.append(visit_node)

    def iterative_deepening(self, max_depth_limit):
        print("Beginning iterative deepening\n")
        for depth_limit in range(1, max_depth_limit):
            print("Depth: {}".format(depth_limit))
            sol_node = self.depth_first_search(depth_limit)
            if sol_node:
                return sol_node
        print("Did not find solution using iterative "
              "deepening with maximum depth to try: {}"
              .format(max_depth_limit))

    def astar_algo(self, depth, heuristic=None):
        self.HEURISTIC = True
        self.open = [(1, 1, self.root_node)]
        self.closed = []
        # turned open list into a list of tuples in the format of (score, node)
        while self.open:
            current_visit = self.open.pop(0)
            visit_node = current_visit[2]

            if self.check_goal_state(visit_node):
                self.HEURISTIC = False
                return visit_node

            if visit_node.depth >= depth:
                print("Skip due to depth")
                continue

            self.closed.append(visit_node)
            children = self.generate_children(visit_node.depth, visit_node)
            fnscore_children = []
            for child in children:
                fnscore_children.append(
                    (child.depth + heuristic(child.board.state),
                     child.board.move_series[-1],
                     child)
                )
            self.open += fnscore_children
            # https://www.programiz.com/python-programming/methods/built-in/sorted
            self.open = sorted(self.open, key=first_two)
            #self.open.sort(key=itemgetter(0))
        self.HEURISTIC = False

    def generate_children(self, parent_depth, parent_node):
        """This function should generate all possible moves except for the move
        that would undo the move that got to this current state: action, check_children()
        will make sure that new board states aren't created that are already in open or closed
        lists"""
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
        for item in self.open:
            if self.HEURISTIC:
                #node = item[1]  # todo this may break Jenny's code cuz tuples of 3 now not 2
                node = item[2]
            else:
                node = item
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
        """This function should recursively add solution nodes board.state and move info to
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

    def manhattan_distance(self, current_state):
        """
        Computes the sum of how far each digit is from its goal position
        :param current_state: current board state gotten from node currently being examined
        :return: int, total manhattan distance
        """

        manhattan_distance = 0

        # compute row diff and col diff of digit's current and goal positions, largest diff = # moves to get to goal
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                # if i > 0:
                #     j_ = j + 1
                # else:
                #     j_ = j
                current_digit = current_state[self.board_cols * i + j]
                goal_position = self.correct_state.index(current_digit)
                goal_position_row = int(goal_position / self.board_cols)
                goal_position_col = goal_position - (self.board_cols * goal_position_row)

                row_diff = abs(goal_position_row - i)
                col_diff = abs(goal_position_col - j)

                # add largest diff to manhattan distance sum
                if row_diff >= col_diff:
                    manhattan_distance += row_diff
                else:
                    manhattan_distance += col_diff

        return manhattan_distance

    def permutation_inversions(self, current_state):
        """
        for each digit, check how many digits on its right should be on its left
        :param current_state:
        :return: total score
        """
        score = 0
        puzzle_size = len(current_state)
        for i in range(puzzle_size - 1):
            goal_position = self.correct_state.index(current_state[i])
            left_sequence = self.correct_state[:goal_position]
            for j in range(i + 1, puzzle_size):
                if current_state[j] in left_sequence:
                    score += 1
        return score

    def hamming_distance(self, current_state):
        score = 0
        for i in range(len(current_state)):
            if self.correct_state[i] != current_state[i]:
                score += 1
        return score

    def best_first_search(self, depth, heuristic=None):
        """
        Best First Search with choice between 2 heuristics
        Heuristic 1: Manhattan distance
        Heuristic 2: Sum of permutation inversions
        :return: final node
        """
        self.HEURISTIC = True
        # self.open = [(1, self.open[0])]  # todo could be a problem if self.open[0] != self.root_node?
        self.open = [(1, 1, self.root_node)]
        # turned open list into a list of tuples in the format of (score, node)
        while self.open:
            current_visit = self.open.pop(0)
            visit_node = current_visit[2]
            # print("Score: ", current_visit[0])
            # print("Depth", visit_node.depth)
            # visit_node.print_node()

            if self.check_goal_state(visit_node):
                self.HEURISTIC = False
                self.open = [self.root_node]
                return visit_node

            self.closed.append(visit_node)

            if visit_node.depth >= depth:
                print("Skip due to depth")
                continue

            children = self.generate_children(visit_node.depth, visit_node)
            for child in children:
                if heuristic == 1:
                    score = self.hamming_distance(child.board.state)
                    self.open.append((score, child.board.move_series[-1], child))
                elif heuristic == 2:
                    score = self.permutation_inversions(child.board.state)  # todo overestimates
                    if score % 2 == 0:
                        self.open.append((score, child.board.move_series[-1], child))
                elif heuristic == 3:
                    score = self.manhattan_distance(child.board.state)
                    self.open.append((score, child.board.move_series[-1], child))
                else:
                    import sys
                    sys.exit('Invalid heuristic function')
                # self.open.append((score + child.depth, child))
                self.open.append((score, child.board.move_series[-1], child))
            self.open = sorted(self.open, key=first_two)
            # print(self.open)


