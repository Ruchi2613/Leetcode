'''1228. Missing Number In Arithmetic Progression
Easy
Topics
conpanies icon
Companies
Hint
In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

A value from arr was removed that was not the first or last value in the array.

Given arr, return the removed value.

 

Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].
 

Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 105
The given array is guaranteed to be a valid array.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,938/61.2K
Acceptance Rate
52.2%'''


class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        diff = (arr[-1] - arr[0]) // n
        
        for i in range(n - 1):
            if arr[i+1] - arr[i] != diff:
                return arr[i] + diff
        
        return arr[0]