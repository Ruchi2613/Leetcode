from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:

        d = {}

        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x]+=1

        maxi = max(d.keys())

        for k , v in d.items():
            if maxi == k:
                if len(nums) != maxi+1:
                    return False


        for i in range(1, maxi):

            if i not in d:
                return False

            if d[i] != 1:
                return False

            
        if maxi not in d:
            return False

        if d[maxi]!= 2:
            return False

        return True            


