from copy import deepcopy


class Board(object):

    letters = ['a', 'b', 'c', 'd',
               'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p',
               'q', 'r', 's', 't']
    UP = 'up'
    UP_RIGHT = 'up_right'
    RIGHT = 'right'
    DOWN_RIGHT = 'down_right'
    DOWN = 'down'
    DOWN_LEFT = 'down_left'
    LEFT = 'left'
    UP_LEFT = 'up_left'

    def __init__(self, cols, rows, state=None):
        self.rows = rows
        self.cols = cols
        self.state = state
        self.move_series = [0]  # to break ties between nodes we need to know the latest move for each
        self.tie_breaker = {
            'UP': 0,
            'UP_RIGHT': 1,
            'RIGHT': 2,
            'DOWN_RIGHT': 3,
            'DOWN': 4,
            'DOWN_LEFT': 5,
            'LEFT': 6,
            'UP_LEFT': 7
        }

    def print_board(self):
        print("=============")
        for i in range(self.rows):
            for j in range(self.cols):
                num = (self.state[i*self.cols + j])
                if num < 10:
                    print("{}   ".format(num), end='')
                else:
                    print("{}  ".format(num), end='')
            print("")
        print("=============\n\n")

    def make_move(self, move):
        """This function takes a move corresponding to the moves listed above
            and returns a state [] and an action for creating a new Node.
            Returns false if move is invalid. ie off board"""
        zero_index = self.state.index(0)
        state = deepcopy(self.state)
        action = None
        new_state = None
        if move is Board.UP:
            new_state = self.up(zero_index, state)
            self.move_series.append(self.tie_breaker['UP']) # todo test these
        elif move is Board.UP_RIGHT:
            new_state = self.up_right(zero_index, state)
            self.move_series.append(self.tie_breaker['UP_RIGHT'])
        elif move is Board.RIGHT:
            new_state = self.right(zero_index, state)
            self.move_series.append(self.tie_breaker['RIGHT'])
        elif move is Board.DOWN_RIGHT:
            new_state = self.down_right(zero_index, state)
            self.move_series.append(self.tie_breaker['DOWN_RIGHT'])
        elif move is Board.DOWN:
            new_state = self.down(zero_index, state)
            self.move_series.append(self.tie_breaker['DOWN'])
        elif move is Board.DOWN_LEFT:
            new_state = self.down_left(zero_index, state)
            self.move_series.append(self.tie_breaker['DOWN_LEFT'])
        elif move is Board.LEFT:
            new_state = self.left(zero_index, state)
            self.move_series.append(self.tie_breaker['LEFT'])
        elif move is Board.UP_LEFT:
            new_state = self.up_left(zero_index, state)
            self.move_series.append(self.tie_breaker['UP_LEFT'])
        else:
            print("\n\n\n\n\nERROR: not a valid board move\n\n\n\n\n")

        if not new_state:
            return False, False

        new_zero_index = new_state.index(0)
        action = deepcopy(Board.letters[new_zero_index])
        return new_state, action

    # Possible board moves
    def up(self, zero_index, state):
        if zero_index < self.cols:
            return False
        # swap_holder = state[zero_index]
        # state[zero_index] = state[zero_index - self.cols]
        # state[zero_index - self.cols] = swap_holder
        Board.swap(state, zero_index, zero_index - self.cols)
        return state

    def right(self, zero_index, state):
        if (zero_index + 1) % self.cols is 0:
            return False
        # swap_holder = state[zero_index]
        # state[zero_index] = state[zero_index +1]
        # state[zero_index - self.cols] = swap_holder
        Board.swap(state, zero_index, zero_index + 1)
        return state

    def up_right(self, zero_index, state):
        if zero_index < self.cols or (zero_index + 1) % self.cols is 0:
            return False
        Board.swap(state, zero_index, zero_index - self.cols + 1)
        return state

    def down(self, zero_index, state):
        limit = len(state) - self.cols - 1
        if zero_index > limit:
            return False
        Board.swap(state, zero_index, zero_index + self.cols)
        return state

    def left(self, zero_index, state):
        if zero_index % self.cols is 0:
            return False
        Board.swap(state, zero_index, zero_index - 1)
        return state

    def down_left(self, zero_index, state):
        limit = len(state) - self.cols - 1
        if zero_index % self.cols is 0 or zero_index > limit:
            return False
        Board.swap(state, zero_index, zero_index + self.cols - 1)
        return state

    def down_right(self, zero_index, state):
        limit = len(state) - self.cols - 1
        if zero_index > limit or (zero_index + 1) % self.cols is 0:
            return False
        Board.swap(state, zero_index, zero_index + self.cols + 1)
        return state

    def up_left(self, zero_index, state):
        if zero_index < self.cols or zero_index % self.cols is 0:
            return False
        Board.swap(state, zero_index, zero_index - self.cols - 1)
        return state

    @staticmethod
    def swap(state, zero_index, swap_index):
        swap_holder = state[zero_index]
        state[zero_index] = state[swap_index]
        state[swap_index] = swap_holder

