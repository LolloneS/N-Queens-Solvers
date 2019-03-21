from random import shuffle, choice
from collections import defaultdict

class Board:
    def __init__(self, n):
        self.n = n
        self.queens = [] # at index K, you get the row in which you have the queen at column K
        '''
        self.queens = [1, 0, 2]
        010
        100
        001
        '''

        # note: here a queen attacks herself!
        # list of the attacks (dictionaries) on the i-th column
        self.constraints = [dict() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.constraints[i][j] = 0



    def __str__(self):
        s = ''
        for i in range(self.n):
            for j in range(self.n):
                if self.queens[j] == i: 
                    s += '1'
                else:
                    s += '0'
            s += '\n'
        return s


    def attacks(self, r1, c1, r2, c2):
        return r1 == r2 or c1 == c2 or abs(r1-r2) == abs(c1-c2)
        
    def get_as_matrix(self):
        # MA intensifies
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.queens[j] == i: 
                    res[i].append(1)
                else:
                    res[i].append(0)
        return res
        # one-liner, but worse performance 
        # return [list(map(int, list(i))) for i in self.__str__().splitlines()]


    def add_queen(self, queen, col=False):
        self.queens.append(queen)
        self.add_queen_constraints(queen, col)

    def get_queen_constraints(self, queen, col):
        return self.constraints[col][queen] - 1   # stiamo togliendo l'attacco a se stessa

    def get_total_queen_constraints(self):
        col = 0
        sumc = 0
        for q in self.queens:
            sumc += self.get_queen_constraints(q, col)
            col += 1
        return sumc // 2   # because attacks are symmetric

    def get_queen(self, col):
        return self.queens[col]
    
    def get_queen_in_row(self, row):
        for col in range(len(self.queens)):
            if self.queens[col] == row:
                return col

    def is_a_solution(self):
        return True if self.get_total_queen_constraints() == 0 and len(self.queens) == self.n else False


    def remove_last_queen(self):
        return self.queens.pop()

    '''
    this function updates the constraints in every cell
    of the board, adding to the dictionary which column is
    forbidden in relation of every row.
    '''
    def add_queen_constraints(self, row, col=False):
        if col == False:
            col = self.get_queen_in_row(row)

        # row and column to avoid 
        for i in range(self.n):
            self.constraints[col][i] += 1
            self.constraints[i][row] += 1         
        
        # remove the duplicate (a queen attacks both her row and her column, remove one)
        self.constraints[col][row] -= 1

        # lower dx diagonal to avoid
        for i in range(min(self.n-col-1, self.n-row-1)):
            self.constraints[col+i+1][row+i+1] += 1
        
        # upper dx diagonal to avoid
        for i in range(min(self.n-col-1, row)):
            self.constraints[col+i+1][row-i-1] += 1

        # upper sx diagonal to avoid
        for i in range(min(col,  row)):
            self.constraints[col-i-1][row-i-1] += 1

        # lower sx diagonal to avoid
        for i in range(min(col, self.n-row-1)):
            self.constraints[col-i-1][row+i+1] += 1





    '''
    this function updates the constraints in every cell
    of the board, removing from the dictionary the locked
    colunm in relation to the row affected by the removed 
    queen
    '''   
    def remove_queen_constraints(self, row, col=False):
        #old_col = col     old_col not 
        if col==False:
            col = self.get_queen_in_row(row)
        self.constraints[col][row] += 1
        
        # row and column to avoid
        for i in range(self.n):
            self.constraints[col][i] -= 1
            self.constraints[i][row] -= 1        
        
        # lower dx diagonal to avoid
        for i in range(min(self.n-col-1, self.n-row-1)):
            # if row+i+1 in self.constraints[col+i+1]:
            self.constraints[col+i+1][row+i+1] -= 1
        
        # upper dx diagonal to avoid
        for i in range(min(self.n-col-1, row)):
            # if row-i-1 in self.constraints[col+i+1]:
            self.constraints[col+i+1][row-i-1] -= 1        

        # upper sx diagonal to avoid
        for i in range(min(col,  row)):
            # if row-i-1 in self.constraints[col-i-1]:
            self.constraints[col-i-1][row-i-1] -= 1

        # lower sx diagonal to avoid
        for i in range(min(col, self.n-row-1)):
            # if row+i+1 in self.constraints[col-i-1]:
            self.constraints[col-i-1][row+i+1] -= 1        


    def swap_rows(self, old_row, old_col, dest_row, dest_col):
        self.remove_queen_constraints(old_row, old_col)
        self.remove_queen_constraints(dest_row, dest_col)
        self.queens[old_col] = dest_row
        self.queens[dest_col] = old_row   
        self.add_queen_constraints(dest_row, old_col)
        self.add_queen_constraints(old_row, dest_col)






