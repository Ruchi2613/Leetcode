class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # count = [0]* len(nums)

        # for x in range(len(nums)):
        #     for y in range(len(nums)):
        #         if nums[y]<nums[x]:
        #             count[x]+=1
        # return count


        d = {}
        res = []
        sorted_list = sorted(nums)
        for i in range(len(nums)):
            if sorted_list[i] not in d:
                d[sorted_list[i]] = i
        # print(d)

        for x in range(len(nums)):
            if nums[x] in d:
                res.append(d[nums[x]])
        
        return res

cl = Solution()
print(cl.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))