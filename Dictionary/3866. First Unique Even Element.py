'''3866. First Unique Even Element
Solved
Easy
Topics
You are given an integer array nums.

Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. If no such integer exists, return -1.

An integer x is considered even if it is divisible by 2.

 

Example 1:

Input: nums = [3,4,2,5,4,6]

Output: 2

Explanation:

Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

Example 2:

Input: nums = [4,4]

Output: -1

Explanation:

No even integer appears exactly once, so return -1.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
46,220/69.7K
Acceptance Rate
66.3%
'''

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d = {}

        for num in nums:
            if num % 2 == 0:
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1

        # print(d)

        for num in nums:
            if num%2 == 0 and d[num] ==1:
                return num

        return -1

