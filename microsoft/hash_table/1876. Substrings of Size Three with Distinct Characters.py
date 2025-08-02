class Solution:
    def countGoodSubstrings(self, s: str) -> int:


        i = j = 0
        k = 3
        d = {}
        res = 0


        while j < k:
            if s[j] not in d:
                d[s[j]]= 1
            else:
                d[s[j]]+=1
            j+=1

            if len(d)== k:
                res+=1

            if len(s) < k:
                return 0

        while j < len(s):
            d[s[i]] -= 1
            if d[s[i]] == 0:
                del d[s[i]]
            i += 1

            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1

            if len(d) == k:
                res += 1
            j += 1

        return res


        # k=3
        # cnt=0

        # for i in range(0,len(s)-k+1):
        #     if len(set(s[i:i+k]))==k:
        #         cnt+=1
        # return cnt


        # result = 0
        # substr = []
        # a = ''
        # k = 3

        # for x in range(len(s)):
        #     substr.append(s[x])

        #     if len(substr) > k:
        #         substr.pop(0)

        #     if len(substr) == k and len(set(substr)) == k:
        #         result += 1

        # return result