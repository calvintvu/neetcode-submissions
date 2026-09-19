class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []
        self.sol = []

        # only add open parentheses if open < n
        # only add a closing parenthese if closed < open
        # valid IFF open == closed == n

        def backtrack(open_cnt, closed_cnt):

            if open_cnt == closed_cnt == n:
                self.res.append("".join(self.sol))
                return
            
            if open_cnt < n:
                self.sol.append("(")
                backtrack(open_cnt + 1, closed_cnt)
                self.sol.pop()
            
            if closed_cnt < open_cnt:
                self.sol.append(")")
                backtrack(open_cnt, closed_cnt + 1)
                self.sol.pop()
        
        backtrack(0, 0)
        return self.res