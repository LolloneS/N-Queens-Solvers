from random import randint, choice, shuffle
import time
from Board import Board
from math import log

class GlobalSearchSolver:
    def __init__(self, n):
        if isinstance(n, Board):
            self.construct_from_board(n) 
        else:
            self.n = n
            self.board = Board(n)
            k = [i for i in range(self.n)]
            shuffle(k)
            for i in range(n):
                self.board.add_queen(k[i], i)
        self.count = 1
    
    def perform_random_move(self):
        c1 = randint(0, self.n-1)
        c2 = randint(0, self.n-1)
        while c1 == c2: # the columns must be different
            c2 = randint(0, self.n-1)
        return c1, c2

    def construct_from_board(self, brd):
        self.n = brd.n
        self.board = brd

    def find_next_move(self):
        if self.board.get_total_queen_constraints() >= 5*log(self.n):
            p = int(log(self.n) ** 2)
        else:
            p = self.n
        max_constraints = self.board.get_queen_constraints(self.board.queens[0], 0)
        chosen_col, best_difference = 0, 0
        chosen_cols, possible_moves, already_checked = [], [], []
        for q in range(self.n):
            if self.board.get_queen_constraints(self.board.queens[q], q) > max_constraints:
                max_constraints = self.board.get_queen_constraints(self.board.queens[q], q)
                chosen_cols = [q]
            elif self.board.get_queen_constraints(self.board.queens[q], q) == max_constraints:
                chosen_cols.append(q)
        shuffle(chosen_cols)
        for chosen_col in chosen_cols:
            chosen_row = self.board.get_queen(chosen_col)
            already_checked.append(chosen_row)
            for row in range(p):
                if row != self.board.queens[chosen_col] and row not in already_checked:
                    other_col = self.board.get_queen_in_row(row)
                    new_constraints = self.board.constraints[chosen_col][row] + self.board.constraints[other_col][chosen_row] - 2
                    old_constraints = self.board.constraints[chosen_col][chosen_row] + self.board.constraints[other_col][row] 
                    if not(self.board.attacks(chosen_row, chosen_col, row, other_col)) and new_constraints < old_constraints:
                        difference = old_constraints - new_constraints # surely >= 0
                        if difference > best_difference:
                            best_difference = difference
                            possible_moves = [(chosen_col, other_col)]
                        elif difference == best_difference:
                            possible_moves.append((chosen_col, other_col))
            if len(possible_moves) > 5: 
                break
        if not possible_moves:
            return self.perform_random_move()
        new_col = choice(possible_moves)
        return new_col


    def solve(self):
        while not self.board.is_a_solution():
            self.count += 1
            old_col, dest_col = self.find_next_move()
            old_row, dest_row = self.board.get_queen(old_col), self.board.get_queen(dest_col)
            self.board.swap_rows(old_row, old_col, dest_row, dest_col)
        return self.board
