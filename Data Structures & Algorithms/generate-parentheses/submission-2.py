class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, open_used, close_used):
            if len(cur) == n * 2:
                res.append(cur)
            
            if open_used < n: # still can add more open
                dfs(cur + '(', open_used + 1, close_used)
            
            if close_used < open_used: # still can add more close
                dfs(cur + ')', open_used, close_used + 1)
            
        dfs('', 0, 0)
        return res
            

