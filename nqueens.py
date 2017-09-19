import matplotlib
import matplotlib.pyplot as plt
import math
#%matplotlib inline
import pprint
import sys


from board import Board

class Backtrack:
    def make_move(self, a, c):
        a.append(c)
    
    def unmake_move(self, a, c):
        a.pop()
    
    def backtrack(self, n, a = []):
        if (self.is_a_solution(a,n)):
            self.process_solution(a)
        else:
            for c in self.construct_candidates(a,n):
                self.make_move(a, c)
                self.backtrack(n,a)
                self.unmake_move(a,c)
                


                
class NQueens(Backtrack):
    """Solves NQueens
    
    We evaulate the symmetries of the system.  The 2D square is a
    representation of Dih4. Using the the generators b = horizontal reflection
    and c = ccw rotation + vertical rotation the Cayley graph has a hamiltonian
    path with the application of the generators in this sequence
    
    e c b c b c b c b -> e

    This means that we can generate all possible 2D square symmetries very
    easily.

    """
    
    def __init__(self, board_size):
        self.result_type = list
        self.board_size = board_size
        self.results = set()
        self.p = 0
        self.bad = set()

    def is_a_solution(self, a,n):
        return len(a) == n

    def process_solution(self, a):
        a = tuple(sorted(tuple(a)))
        self.results.add(a)

    def construct_candidates(self, a, n):
        board = self.position_list_to_board(a)

        self.print_board(board)
        sys.exit(0)
        
        op = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == NQueens.OPEN:
                    op.append((i,j))       
        
        
        if len(op) + len(a) < n:
            # Then there's no point, we don't have enough candidates to get to n
            return []        
        return op


    
    def print_board(self, board):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        img = ax.imshow(board, vmin=0, vmax=2)
        #ax.set_axis_off()
        ax.set_xticks(np.arange(-.5, self.board_size, 1), minor=True);
        ax.set_yticks(np.arange(-.5, self.board_size, 1), minor=True);
        ax.set_yticklabels([], minor=True)
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
        plt.show()
    
    def print_results(self):
        
        nresults = len(self.results)
        
        print "N=", nresults
        
        pprint.pprint(self.bad)
        
        ncol = 1 if nresults > 1 else nresults
        nrow = nresults/ncol + nresults % ncol
        
        print ncol, nrow,
        
        
        fig = plt.figure()
        
        plt.axis('off')
        for i,r in enumerate(self.results):
            board = self.position_list_to_board(r)
            ax = fig.add_subplot(nrow, ncol, i+1)
            img = ax.imshow(board)
            ax.set_axis_off()
        
        plt.show()
        
        
    def backtrack(self, n, a = []):
        if (self.is_a_solution(a,n)):
            self.process_solution(a)
            return 1
        
        b = 0
        for c in self.construct_candidates(a,n):
            self.make_move(a, c)
            
            v = self.backtrack(n,a)
            if v == 0:
                self.bad.add(tuple(sorted(tuple(a))))
            b += v
            self.unmake_move(a,c)
        return b
    
NQ = NQueens(4)


# e = NQ.create_board()
# NQ.place_queen(1,2,e)
# NQ.place_queen(0,0,e)
# NQ.print_board(e)

# pprint.pprint(e)

# print NQ.board_to_position_list(e)

NQ.backtrack(4)

NQ.print_results()
plt.show()
