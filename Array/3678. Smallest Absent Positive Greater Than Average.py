'''3678. Smallest Absent Positive Greater Than Average
Solved
Easy
Topics
Hint
You are given an integer array nums.

Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements in nums.

The average of an array is defined as the sum of all its elements divided by the number of elements.
 

Example 1:

Input: nums = [3,5]

Output: 6

Explanation:

The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
The smallest absent positive integer greater than 4 is 6.
Example 2:

Input: nums = [-1,1,2]

Output: 3

Explanation:

​​​​​​​The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
The smallest absent positive integer greater than 0.667 is 3.
Example 3:

Input: nums = [4,-1]

Output: 2

Explanation:

The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50.
The smallest absent positive integer greater than 1.50 is 2.
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100​​​​​​​
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
37,220/108.7K
Acceptance Rate
34.2%'''


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        # avg = sum(nums) / len(nums)
        # i = int(avg) + 1

        # while True:
        #     if i > 0 and i not in nums:
        #         return i
        #     i += 1

        n=sum(nums)//len(nums)
        if n<0:
            n=1
        else:
            n+=1
        while n:
            if n not in nums:
                return n
            else:
                n+=1