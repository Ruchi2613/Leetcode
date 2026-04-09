'''3487. Maximum Unique Subarray Sum After Deletion
Easy
Topics
conpanies icon
Companies
Hint
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

 

Example 1:

Input: nums = [1,2,3,4,5]

Output: 15

Explanation:

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:

Input: nums = [1,1,0,1,1]

Output: 1

Explanation:

Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:

Input: nums = [1,2,-1,-2,1,0,-1]

Output: 3

Explanation:

Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
157,747/389.8K
Acceptance Rate
40.5%'''

class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sett = set()
        # neg = set()

        # for x in nums:
        #     if x >= 0:
        #         sett.add(x)
        #     else:
        #         neg.add(x)

        # if len(sett)!= 0:
        #     return sum(sett)
        # else:
        #     l = list(neg)
        #     l.sort()
        #     return l[-1]
        # 2nd solution:
        sum = 0
        st = set()
        mxNeg = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                st.add(nums[i])
            else:
                mxNeg = max(mxNeg, nums[i])
        for val in st:
            sum += val
        if len(st) > 0:
            return sum
        else:
            return mxNeg

