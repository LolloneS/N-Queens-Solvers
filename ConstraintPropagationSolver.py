from Board import Board
from random import randint, choice
from collections import defaultdict
import time

class ConstraintPropagationSolver:
    def __init__(self, n):
        self.board = Board(n)
        self.n = n
        self.backtracked_queens = [[] for _ in range(self.n)]
        self.count = 1 # for benchmarking purposes



    '''
    after adding the first queen we update the constraints, then we 
    che if we have a legal move in the next row.
    if the answer is yes we proceed adding a new queen updating the
    constraints, otherwise we backtrack removing the queen, the constraints 
    and adding the queen to the list of legal moves that we have already tried.
    if we backtrack two times in a row we need to reset the list of the legal
    moves that we avoided before because we will arrive to that move with 
    another configuration.
    '''
    def solve(self):
        first_queen = randint(0, self.n-1)
        self.board.add_queen(first_queen)
        col = 1

        while not self.board.is_a_solution():
            self.count += 1
            col_constraints = 0
            for i in range(self.n):
                if(self.board.constraints[col][i]) != 0:
                    col_constraints += 1

            if col_constraints + len(self.backtracked_queens[col]) >= self.n:
                r = self.board.get_queen(col-1)
                self.board.remove_queen_constraints(r)
                self.backtracked_queens[col-1].append(r)
                self.backtracked_queens[col] = []
                col -= 1
                self.board.remove_last_queen()
                
            else:
                moves = [k for k, v in self.board.constraints[col].items() if v == 0 and k not in self.backtracked_queens[col]]             
                new_queen = choice(moves)
                self.board.add_queen(new_queen)
                col += 1
        
        return self.board
         
