class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        # res = []
        # k = 3
        # subst = []

        # for x in range(len(s)):
        #     if len(s[x:x+k]) == k:
        #         subst.append(s[x:x+k])
        
        # for word in subst:
        #     if len(set(word)) == len(word):
        #         res.append(word)

        # return len(res)


        # sliding window

        i = j = 0
        k = 3
        d = {}
        res = 0

        while j < k:
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]]+=1
            
            j+=1


        if len(d) == k:
            res+=1
        
        if len(s)<k:
            return 0
        
        while j < len(s):
            d[s[i]]-=1
            if d[s[i]] == 0:
                del d[s[i]]

            i+=1

            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] +=1

            j+=1

            if len(d) == k:
                res+=1

        return res

cl = Solution()
print(cl.countGoodSubstrings(s = "aababcabc"))