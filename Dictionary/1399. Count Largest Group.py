'''1399. Count Largest Group
Easy
Topics
conpanies icon
Companies
Hint
You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104'''


class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        d = {}
        
        '''i = 1,2,3,4,5,6,7,8,9
        1+0 == 1
        1+1 = 2
        
        1 = [1,10]
        2 = [2,11]
        if n = 123
        if n > 1:
            for i in range(str(n)):
                sum +=int(i)
                 i.e 1+2+3 = 6 
        1+2+3 = 6 = [3,13,123]'''

        # n = str(1243)
        # print(len(n))
        for x in range(1,n+1):
            if len(str(x)) == 1:
                d[x] = [x]

            elif len(str(x))>1:
                sum_y = 0
                n = str(x)
                for y in n:
                    sum_y = sum_y+int(y)

                if sum_y in d:
                    d[sum_y].append(int(n))
                else:
                    d[sum_y] = [int(n)]
            else:
                d[x].append(x)
        
        maximum = max(len(v) for v in d.values())
        print(maximum)

        count= 0

        for k , v in d.items():
            if len(v) == maximum:
                count+=1
        

        return count




