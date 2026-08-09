class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = -1
        start = 0
        hist = dict()
        for idx, c in enumerate(s):
            if c in hist:
                if idx - start > longest_len:
                    longest_len = idx - start
                start = hist[c] + 1 # 1 after the repeated
            hist[c] = idx
        
        return longest_len