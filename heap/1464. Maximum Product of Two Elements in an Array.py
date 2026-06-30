'''1464. Maximum Product of Two Elements in an Array
Solved
Easy
Topics
conpanies icon
Companies
Hint
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12'''


import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max1 = max(nums)
        # nums.remove(max1)
        # max2 = max(nums)

        # return (max1 - 1) * (max2 - 1)


        # maxheap = []

        # for num in nums:
        #     heapq.heappush(maxheap, -num)

        # max1 = -heapq.heappop(maxheap)
        # max2 = -heapq.heappop(maxheap)

        # return (max1 - 1) * (max2 - 1)
    

        for i in range(len(nums)):
            nums[i] = -nums[i]
        

        heapq.heapify(nums)
        print(nums)

        frst_num = -heapq.heappop(nums)
        sec_num = -heapq.heappop(nums)

        return (frst_num-1) * (sec_num-1)


