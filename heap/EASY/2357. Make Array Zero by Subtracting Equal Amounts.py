'''2357. Make Array Zero by Subtracting Equal Amounts
Solved
Easy
Topics
Hint
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

 

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
'''

import heapq
import sys
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        if len(set(nums)) == 1:
            if 0 in nums:
                return 0
            else:
                return 1

        count = 0 

        while len(set(nums)) != 1:
            mini_num = sys.maxsize

            for n in nums:
                if n!= 0:
                    mini_num = min(mini_num,n)

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= mini_num

            count +=1

        return count




        
            