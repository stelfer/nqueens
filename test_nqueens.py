import unittest

from nqueens import NQueens

class TestNQueens(unittest.TestCase):
    def test_it(self):
    
        NQ = NQueens(6)
        NQ.backtrack(6)
        NQ.print_results()

        
if __name__ == '__main__':
    unittest.main()
