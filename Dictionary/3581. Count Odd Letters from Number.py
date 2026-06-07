'''3581. Count Odd Letters from Number
Solved
Easy
Topics
Hint
You are given an integer n perform the following steps:

Convert each digit of n into its lowercase English word (e.g., 4 → "four", 1 → "one").
Concatenate those words in the original digit order to form a string s.
Return the number of distinct characters in s that appear an odd number of times.

 

Example 1:

Input: n = 41

Output: 5

Explanation:

41 → "fourone"

Characters with odd frequencies: 'f', 'u', 'r', 'n', 'e'. Thus, the answer is 5.

Example 2:

Input: n = 20

Output: 5

Explanation:

20 → "twozero"

Characters with odd frequencies: 't', 'w', 'z', 'e', 'r'. Thus, the answer is 5.

 

Constraints:

1 <= n <= 109'''

from typing import Counter


class Solution:
    def countOddLetters(self, n: int) -> int:
        
        d = {
            '0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", 
            '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
        
        a = ''

        
        for x in str(n):
            if x in d:
                a = a+d[x]
        
        cntr = Counter(a)
        cnt = 0
        
        for k, v in cntr.items():
            if v %2!= 0:
                cnt+=1
        
        return cnt
            


                    

