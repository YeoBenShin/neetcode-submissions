class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f_check(test):
            count = 0
            for i in test:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                if count < 0 or count > n:
                    return False
            if count != 0:
                return False
            return True
        
        def mid_check(test):
            count = 0
            for i in test:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                if count < 0 or count > n:
                    return False
            return True

        acceptable = []
        def dfs(c_str):
            if len(c_str) == n * 2:
                if f_check(c_str):
                    acceptable.append(c_str)
                return
            if not mid_check(c_str):
                return 
            dfs(c_str + '(')
            dfs(c_str + ')')
        dfs("")
        return acceptable