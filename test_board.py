import unittest
import copy
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
        ql = ((1,2), (2,0))
        b = Board.from_queen_list(ql, 4)
        self.assertEqual(b.M, [[2, 2, 4, 2], [4, 4, 1, 2], [1, 4, 4, 4], [4, 2, 2, 0]])
        self.assertEqual(ql, b.to_queen_list())
        
        
    def test_open_position(self):
        b = Board(4)
        b.place_queen(2,0)
        b.place_queen(1,2)
        self.assertEqual(b.M, [[2, 2, 4, 2], [4, 4, 1, 2], [1, 4, 4, 4], [4, 2, 2, 0]])
        b.unplace_queen(2,0)
        self.assertEqual(b.M, Board.from_queen_list([(1,2)],4).M)

    def test_reflect_horiz(self):
        b = Board(4)
        b.place_queen(0,0)
        M1 = b.M
        self.assertEqual(M1, [[1, 2, 2, 2], [2, 2, 0, 0], [2, 0, 2, 0], [2, 0, 0, 2]])
        b.reflect_horiz()
        M2 = b.M
        self.assertEqual(M2, [[2, 2, 2, 1], [0, 0, 2, 2], [0, 2, 0, 2], [2, 0, 0, 2]])
        b.reflect_horiz()
        self.assertEqual(b.M, M1)

    def test_reflect_diag_symmetric(self):
        b = Board(4)
        b.place_queen(0,0)
        M1 = b.M
        self.assertEqual(M1, [[1, 2, 2, 2], [2, 2, 0, 0], [2, 0, 2, 0], [2, 0, 0, 2]])
        b.reflect_diag()
        self.assertEqual(b.M, M1)

    def test_reflect_diag_asymmetric(self):
        b = Board(4)
        b.place_queen(1,0)
        M1 = b.M
        self.assertEqual(M1, [[2, 2, 0, 0], [1, 2, 2, 2], [2, 2, 0, 0], [2, 0, 2, 0]])
        b.reflect_diag()
        self.assertEqual(b.M, [[2, 1, 2, 2], [2, 2, 2, 0], [0, 2, 0, 2], [0, 2, 0, 0]])
        b.reflect_diag()
        self.assertEqual(b.M, M1)

    def test_cycle_manual(self):
        b = Board(4)
        b.place_queen(1,0)
        M1 = b.M
        b.reflect_diag()
        b.reflect_horiz()
        b.reflect_diag()
        b.reflect_horiz()
        b.reflect_diag()
        b.reflect_horiz()
        b.reflect_diag()
        b.reflect_horiz()
        self.assertEqual(b.M, M1)

    def test_cycle(self):
        b = Board(4)
        b.place_queen(1,0)
        M1 = b.M
        [ c() for c in b.cycle ]
        self.assertEqual(b.M, M1)

    def test_self_iso(self):
        b = Board(4)
        b.place_queen(1,0)
        b2 = Board(4)
        b2.place_queen(1,0)
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_diag()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_horiz()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_diag()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_horiz()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_diag()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_horiz()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_diag()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)
        b2.reflect_horiz()
        self.assertEqual(b.count_isomorphisms_to(b2), 1)

    def test_no_iso(self):
        b1 = Board(4)
        b1.place_queen(1,0)
        b2 = Board(4)
        b2.place_queen(3,3)
        self.assertEqual(b1.count_isomorphisms_to(b2), 0)
        self.assertEqual(b2.count_isomorphisms_to(b1), 0)        


    def test_iso_in(self):
        b0 = Board(4)
        b0.place_queen(1,0)
        
        ql = b0.to_queen_list()
        s = set()
        s.add(ql)

        b1 = Board(4)
        b1.place_queen(3,0) # 3,0 not isomoporphic to (1,0)
        s.add(b1)

        self.assertTrue(ql in s)
        self.assertEqual(b0.count_isomorphisms_in(s), 1)
        
        
if __name__ == '__main__':
    unittest.main()

    
