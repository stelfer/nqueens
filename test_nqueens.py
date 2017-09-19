import unittest

from nqueens import NQueens

class TestNQueens(unittest.TestCase):
    def test_it(self):
    
        NQ = NQueens(7)
        NQ.backtrack(7)
        NQ.print_results()

        
if __name__ == '__main__':
    unittest.main()
