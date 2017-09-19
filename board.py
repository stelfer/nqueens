import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Board:
    """A generic board class that can evaluate symmetries

    We evaulate the symmetries of the system.  The 2D square is a
    representation of Dih4. Using the the generators 
    
    b = horizontal reflection
    c = ccw rotation + vertical rotation / diagonal reflection

    the Cayley graph has a hamiltonian path with the application of the 
    generators in this sequence
    
    e c b c b c b c b -> e

    This means that we can generate all possible 2D square symmetries very
    easily.

    """

    def __init__(self, size):
        self.size = size
        self.M = [ [ 0 for i in range(self.size)] for j in range(self.size)]
        self.cycle = (self.reflect_diag,
                      self.reflect_horiz,
                      self.reflect_diag,
                      self.reflect_horiz,
                      self.reflect_diag,
                      self.reflect_horiz,
                      self.reflect_diag,
                      self.reflect_horiz)

    @staticmethod
    def from_queen_list(ql, N):
        """Factory from queen_list
        """
        board = Board(N)
        for x in ql:
            board.place_queen(x[0],x[1])
        return board
                    
    def incr_position(self, i,j, incr):
        for k in range(self.size):
            if k != j:
                self.M[i][k] += incr
            if k != i:
                self.M[k][j] += incr
            d0 = (i+k,j+k) if i+k < self.size and j+k < self.size else None
            d1 = (i+k,j-k) if i+k < self.size and j-k > -1 else None
            d2 = (i-k,j+k) if i-k > -1 and j+k < self.size else None
            d3 = (i-k,j-k) if i-k > -1 and j-k > -1 else None
            for d in (d0,d1,d2,d3):
                if d is not None and d != (i,j):
                    l,m = d
                    self.M[l][m] += incr

    def unplace_queen(self, i,j):
        assert(i >= 0 and i < self.size)
        assert(j >= 0 and j < self.size)
        assert(self.M[i][j] == 1)
        self.incr_position(i,j, -2)
        self.M[i][j] = 0
        
    def place_queen(self, i,j):
        assert(i >= 0 and i < self.size)
        assert(j >= 0 and j < self.size)
        assert(self.M[i][j] == 0)
        self.incr_position(i,j, 2)
        assert(self.M[i][j] == 0)
        self.M[i][j] = 1
        
    def to_queen_list(self):
        pl = []
        for i,c in enumerate(self.M):
            for j,r in enumerate(c):
                if r == 1:
                    pl.append((i,j))
        return tuple(pl)

    def reflect_horiz(self):
        K = [ [ self.M[j][i] for i in range(self.size-1,-1,-1)] for j in range(self.size)]
        self.M = K


    def get_reflect_horiz_map(self):
        K = [ [ ((i,j),(j,i)) for i in range(self.size-1,-1,-1)] for j in range(self.size)]
        print K
        D = {}
        for i,c in enumerate(K):
            for j,(k,v) in enumerate(c):
                D[k] = v
        return D                
        
    def reflect_diag(self):
        K = [ [ self.M[j][i] for j in range(self.size)] for i in range(self.size)]
        self.M = K

    def get_reflect_diag_map(self):
        K = [ [ ((i,j),(i,j)) for j in range(self.size)] for i in range(self.size)]
        print K
        D = {}
        for i,c in enumerate(K):
            for j,(k,v) in enumerate(c):
                D[k] = v
        return D                
        
    def get_isomorphisms_in(self, s):
        """This happens by queen list, for efficiency
        
        s is a set
        """
        r = []
        for c in self.cycle:
            c()
            ql = self.to_queen_list()
            if ql in s:
                r.append(ql)
        return tuple(r)
        
    def count_isomorphisms_to(self, board):
        r = 0
        for c in self.cycle:
            c()
            if board.M == self.M:
                r += 1
        return r

    def add_isomorphisms_to(self, s):
        for c in self.cycle:
            c()
            s.add(self.to_queen_list())
    
    def display(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        cmap = plt.cm.jet

        mmax = max([ max(x) for x in self.M ])
        img = ax.imshow(self.M, vmin=0, vmax=mmax, interpolation='nearest')
        cbar = fig.colorbar(img)

        #ax.set_axis_off()
        ax.set_xticks(np.arange(-.5, self.size, 1), minor=True);
        ax.set_yticks(np.arange(-.5, self.size, 1), minor=True);
        ax.set_yticklabels([], minor=True)
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
        plt.show()
    

