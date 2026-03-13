import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        max_len = -sys.maxsize

        for r in range(len(s)):
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1 
            d[s[r]] = r 
            max_len = max(max_len, r - l + 1)

        if len(s) == 0:
            return 0
        else:
            return max_len