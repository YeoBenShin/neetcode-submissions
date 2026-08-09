class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        start = 0
        hist = dict()

        for idx, c in enumerate(s):
            current_len = idx - start
            if current_len > longest_len:
                longest_len = current_len
            if c in hist:
                start = hist[c] + 1 # 1 after the repeated

            hist[c] = idx
        return longest_len