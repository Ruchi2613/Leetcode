import sys


class Solution:
    def largestUniqueNumber(self, nums) -> int:
        
        d = {}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]= 1
        # print(d)
        maxi = -sys.maxsize

        for k, v in d.items():
            if v == 1:
                maxi = max(maxi, k)
        
        if maxi == -sys.maxsize:
            return -1
        else:
            return maxi

cl = Solution()
print(cl.largestUniqueNumber(nums = [5,7,3,9,4,9,8,3,1]))