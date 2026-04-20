'''1287. Element Appearing More Than 25% In Sorted Array
Solved
Easy
Topics
conpanies icon
Companies
Hint
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105'''

from collections import defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
            
        target = len(arr) / 4
        for key, value in counts.items():
            if value > target:
                return key
            
        return -1