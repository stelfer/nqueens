import unittest

from nqueens import NQueens

class TestNQueens(unittest.TestCase):
    def test_it(self):
    
        NQ = NQueens(5)
        NQ.backtrack(5)
        NQ.print_results()

        
if __name__ == '__main__':
    unittest.main()
