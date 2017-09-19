class Backtrack:
    """This is the skeleton for every backtracking algorithm
    """
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
