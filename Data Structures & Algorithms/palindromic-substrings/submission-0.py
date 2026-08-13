class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.isPali(i, i, s)
            count += self.isPali(i, i+1, s)
        return count
        
    def isPali(self, l, r, s):
        count = 0
        length = len(s)
        while l >= 0 and r < length and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
