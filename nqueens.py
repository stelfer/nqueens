import matplotlib
import matplotlib.pyplot as plt
import math
#%matplotlib inline
import pprint
import sys
import copy

from board import Board
from backtrack import Backtrack
                
class NQueens(Backtrack):
    """Solves NQueens

    We prune by testing each candidate against all isomorphisms under Dih4 for
    each known bad position.

    """
    
    def __init__(self, board_size):
        self.result_type = list
        self.board_size = board_size
        self.results = set()
        self.p = 0
        self.bad = set()
        self.bad_isos = 0

    def is_a_solution(self, a,n):
        return len(a) == n

    def process_solution(self, a):
        a = tuple(sorted(tuple(a)))
        self.results.add(a)

    def construct_candidates(self, a, n):
        b = Board.from_queen_list(a, self.board_size)
        c = []
        # Search the board for open positions
        for i in range(self.board_size):
            for j in range(self.board_size):
                if b.M[i][j] == 0:
                    b.place_queen(i,j)
                    if b.count_isomorphisms_in(self.bad) == 0:
                        c.append((i,j))
                    else:
                        self.bad_isos += 1
                    b.unplace_queen(i,j)
        
        if len(c) + len(a) < n:
            # Then there's no point, we don't have enough candidates to get to n
            return []        
        return c

    def backtrack(self, n, a = []):
        if (self.is_a_solution(a,n)):
            self.process_solution(a)
            return 1
        
        b = 0
        for c in self.construct_candidates(a,n):
            self.make_move(a, c)
            
            v = self.backtrack(n,a)
            if v == 0:
                # print "BAD", Board.from_queen_list(a, self.board_size).M
                self.bad.add(tuple(sorted(tuple(a))))
            b += v
            self.unmake_move(a,c)
        return b

    
    def print_results(self):
        nresults = len(self.results)
        print "N=", nresults
        print "Bad_isos = ", self.bad_isos
        if nresults == 0:
            return
        pprint.pprint(self.bad)
        
        ncol = 1 if nresults > 1 else nresults
        nrow = nresults/ncol + nresults % ncol
        print ncol, nrow,
        fig = plt.figure()
        plt.axis('off')
        for i,r in enumerate(self.results):
            board = Board.from_queen_list(r, self.board_size)
            ax = fig.add_subplot(nrow, ncol, i+1)
            img = ax.imshow(board.M)
            ax.set_axis_off()
        plt.show()
        
