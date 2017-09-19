import unittest

from board import Board


class TestBoardBase(unittest.TestCase):


    def test_empty(self):
        b = Board(4)
        V = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(b.M, V)


    def test_bounds(self):
        import itertools
        b = Board(4)
        x = (-100,-1,0,4,100)
        for p in itertools.permutations(x,2):
            with self.assertRaises(AssertionError):
                b.place_queen(*p)

    def test_single_placement(self):

        D = { (0,0) : [[1, 2, 2, 2], [2, 2, 0, 0], [2, 0, 2, 0], [2, 0, 0, 2]],
              (0,1) : [[2, 1, 2, 2], [2, 2, 2, 0], [0, 2, 0, 2], [0, 2, 0, 0]],
              (0,2) : [[2, 2, 1, 2], [0, 2, 2, 2], [2, 0, 2, 0], [0, 0, 2, 0]],
              (0,3) : [[2, 2, 2, 1], [0, 0, 2, 2], [0, 2, 0, 2], [2, 0, 0, 2]],
              (1,0) : [[2, 2, 0, 0], [1, 2, 2, 2], [2, 2, 0, 0], [2, 0, 2, 0]],
              (1,1) : [[2, 2, 2, 0], [2, 1, 2, 2], [2, 2, 2, 0], [0, 2, 0, 2]],
              (1,2) : [[0, 2, 2, 2], [2, 2, 1, 2], [0, 2, 2, 2], [2, 0, 2, 0]],
              (1,3) : [[0, 0, 2, 2], [2, 2, 2, 1], [0, 0, 2, 2], [0, 2, 0, 2]],
              (2,0) : [[2, 0, 2, 0], [2, 2, 0, 0], [1, 2, 2, 2], [2, 2, 0, 0]],
              (2,1) : [[0, 2, 0, 2], [2, 2, 2, 0], [2, 1, 2, 2], [2, 2, 2, 0]],
              (2,2) : [[2, 0, 2, 0], [0, 2, 2, 2], [2, 2, 1, 2], [0, 2, 2, 2]],
              (2,3) : [[0, 2, 0, 2], [0, 0, 2, 2], [2, 2, 2, 1], [0, 0, 2, 2]], 
              (3,0) : [[2, 0, 0, 2], [2, 0, 2, 0], [2, 2, 0, 0], [1, 2, 2, 2]],
              (3,1) : [[0, 2, 0, 0], [0, 2, 0, 2], [2, 2, 2, 0], [2, 1, 2, 2]],
              (3,2) : [[0, 0, 2, 0], [2, 0, 2, 0], [0, 2, 2, 2], [2, 2, 1, 2]],
              (3,3) : [[2, 0, 0, 2], [0, 2, 0, 2], [0, 0, 2, 2], [2, 2, 2, 1]]
        }

        for k,v in D.iteritems():
            b = Board(4)
            b.place_queen(*k)
            # print k,b.M
            # b.display()
            self.assertEqual(b.M, v)

    def test_multiple_placement(self):
        b = Board(4)
        b.place_queen(2,0)
        b.place_queen(1,2)
        self.assertEqual(b.M, [[2, 2, 4, 2], [4, 4, 1, 2], [1, 4, 4, 4], [4, 2, 2, 0]])

    def test_from_queen_list(self):
        ql = [(1,2), (2,0)]
        b = Board.from_queen_list(ql, 4)
        self.assertEqual(b.M, [[2, 2, 4, 2], [4, 4, 1, 2], [1, 4, 4, 4], [4, 2, 2, 0]])
        
    def test_open_position(self):
        b = Board(4)
        b.place_queen(2,0)
        b.place_queen(1,2)
        self.assertEqual(b.M, [[2, 2, 4, 2], [4, 4, 1, 2], [1, 4, 4, 4], [4, 2, 2, 0]])
        b.unplace_queen(2,0)
        self.assertEqual(b.M, Board.from_queen_list([(1,2)],4).M)
        

if __name__ == '__main__':
    unittest.main()

    
