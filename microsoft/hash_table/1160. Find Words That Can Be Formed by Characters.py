from collections import defaultdict


class Solution:
    def countCharacters(self, words, chars):
        
        d = defaultdict(int)

        for ch in chars:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        # print(d)
        count_res = 0
        for ch in words:
            d1 = defaultdict(int)
            for c in ch:
                if c in d:
                    d1[c]+=1
                else:
                    d1[c]=1

            good = True
            for chh, freq in d1.items():
                if d[chh] < freq:
                    good = False
                    break
            
            if good:
                count_res+=len(ch)
        return count_res   
cl= Solution()
print(cl.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))   