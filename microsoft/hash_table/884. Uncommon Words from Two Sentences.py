class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        
        word1 = s1.split()
        word2 = s2.split()
        # print(s,t)
        d = {}
        res = []
        for w in word1:
            if w in d:
                d[w]+=1
            else:
                d[w]=1

        for w in word2:
            if w in d:
                d[w]+=1
            else:
                d[w]=1

        for k,v in d.items():
            if v == 1:
                res.append(k)

        return res
cl = Solution()
print(cl.uncommonFromSentences())