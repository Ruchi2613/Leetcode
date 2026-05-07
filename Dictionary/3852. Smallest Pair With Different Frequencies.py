'''3852. Smallest Pair With Different Frequencies
Easy
Topics
Hint
You are given an integer array nums.

Consider all pairs of distinct values x and y from nums such that:

x < y
x and y have different frequencies in nums.
Among all such pairs:

Choose the pair with the smallest possible value of x.
If multiple pairs have the same x, choose the one with the smallest possible value of y.
Return an integer array [x, y]. If no valid pair exists, return [-1, -1].

 

Example 1:

Input: nums = [1,1,2,2,3,4]

Output: [1,3]

Explanation:

The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is [1, 3].

Example 2:

Input: nums = [1,5]

Output: [-1,-1]

Explanation:

Both values have the same frequency, so no valid pair exists. Return [-1, -1].

Example 3:

Input: nums = [7]

Output: [-1,-1]

Explanation:

There is only one value in the array, so no valid pair exists. Return [-1, -1].

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
37,874/54.5K
Acceptance Rate
69.5%'''

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:

        class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d ={}

        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        sett = sorted(d.keys())

        # print(d)
        dist_list = []
        for i in range(len(sett)):
            for j in range(i+1,len(sett)):
                dist_list.append([sett[i],sett[j]])

        # print(dist_list)

        freq_distinct_list = []
        for x in dist_list:
            e1 , e2 = x[0],x[1]
            if d[e1]!= d[e2]:
                freq_distinct_list.append([e1,e2])
        print(freq_distinct_list)


        if len(freq_distinct_list) == 0:
            return [-1,-1]

        
        res = freq_distinct_list[0]


        return res

            
