class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        l = r = 0
        max_len = 0
        d = {}

        while r < len(s):

            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]]+=1

            while d[s[r]] > 2:
                d[s[l]]-=1
                if d[s[l]] == 0:
                    del d[s[l]]
                l+=1

            max_len = max(max_len, r-l+1)

            r+=1

        return max_len