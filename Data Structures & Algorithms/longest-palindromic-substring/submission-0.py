class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        # longest_len = -1
        # longest_s = ""
        # idx = 0
        # pos = 1
        # l = len(s)
        # while idx < l:
        #     if pos + 1 < l and self.isPali(s[idx : pos + 1]):
        #         if (len(s[idx:pos+1]) > longest_len):
        #             longest_len = len(s[idx:pos+1])
        #             longest_len = s[idx:pos+1]
        #             pos += 1
        #         else:
        #             pos = 1
        #             idx += 1
        # return longest_s  
        res = ""
        resLen = -1
        length = len(s)
        for i in range(length):
            # odd
            l, r, oLen = self.paliLen(i, i, length, s)
            if oLen > resLen:
                resLen = oLen
                res = s[l+1:r]
            
            # even 
            l, r, oLen = self.paliLen(i-1, i, length, s)
            if oLen > resLen:
                resLen = oLen
                res = s[l+1:r]
        return res
            

    def paliLen(self, l, r, length, s):
        while (l >= 0 and r < length and s[l] == s[r]):
            l -= 1
            r += 1
        return l, r, r - l + 1

       
    # brute force
    # def isPali(self, s):
    #     l = 0
    #     r = len(s) - 1
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True