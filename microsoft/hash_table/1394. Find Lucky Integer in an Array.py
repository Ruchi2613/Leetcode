class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        d = {}

        for x in arr:
            if x in d:
                d[x]+=1
            else:
                d[x]= 1

        ans = -1
        for k , v in d.items():
            if k == v and k > ans:
                ans = k

        return ans