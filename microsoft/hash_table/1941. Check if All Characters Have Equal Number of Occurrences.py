class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d ={}

        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        # print(d)

        set_res = set()
        for v in d.values():
            set_res.add(v)

        if len(set_res) ==1:
            return True
        
        return False