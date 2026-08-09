class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        start = 0
        hist = dict()
        # if len(s) == 1:
        #     return 1

        for idx, c in enumerate(s):
            current_len = idx - start
            if c in hist:
                if hist[c] >= start: # the rest in the past can be ignored
                    start = hist[c] + 1 # 1 after the repeated
                else:
                    current_len += 1 # character is accepeted
            if c not in hist:
                current_len += 1 # character is accepeted
            if current_len > longest_len:
                longest_len = current_len
            hist[c] = idx
        return longest_len