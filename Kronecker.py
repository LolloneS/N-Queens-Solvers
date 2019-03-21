from scipy import sparse
import numpy as np
from collections import defaultdict
from Factorizer import Factorizer
from Board import Board
from ConstraintPropagationSolver import ConstraintPropagationSolver
from LocalSearchSolver import LocalSearchSolver
from GlobalSearchSolver import GlobalSearchSolver

class Kronecker:
    def __init__(self, n, method="CP", print_board=False):
        self.n = n
        self.print_board = print_board
        if method == 'CP':
            self.method="CP"
        else:
            self.method = "GS"
            
    
    def solve(self):
        factors = Factorizer(self.n).factorize()
        intermediate, couples = [], {}        
        if self.method == 'CP':
            for k, _ in factors.items():
                couples[k] = ConstraintPropagationSolver(k).solve()
        else:
            for k, _ in factors.items():
                couples[k] = GlobalSearchSolver(k).solve()

        solved_clean = {k: v.get_as_matrix() for k, v in couples.items()}

        for _, j in solved_clean.items(): j = sparse.csr_matrix(np.array(j))

        for number, solution in solved_clean.items():
            for i in range(factors[number]-1):
                solution = sparse.csr_matrix(solution)
                solution = sparse.kron(solved_clean[number], solution).toarray()
            intermediate.append(solution)
        
        for _ in range(len(intermediate)-1):
            s0 = sparse.csr_matrix(np.array(intermediate[0]))
            s1 = sparse.csr_matrix(np.array(intermediate[1]))
            intermediate[0] = sparse.kron(s0, s1).toarray()
            intermediate.remove(intermediate[1])

        if self.print_board == False:
            result = Board(self.n)
            for i in range(len(intermediate[0])):
                for j in range(len(intermediate[0])):
                    if (intermediate[0][j][i] == 1):
                        result.add_queen(j) 
            return result
        



