'''1427. Perform String Shifts
Easy
Topics
conpanies icon
Companies
Hint
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [directioni, amounti]:

directioni can be 0 (for left shift) or 1 (for right shift).
amounti is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
directioni is either 0 or 1.
0 <= amounti <= 100'''


from ast import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        temp = list(s)

        l , r = 0,1

        for x in shift:
            direction, amt = x[0], x[1]

            if direction == l:
                for amount in range(amt):
                    first_ele = temp.pop(0)
                    temp.append(first_ele)
            else:
                for amount in range(amt):
                    last_ele = temp.pop()
                    temp.insert(0,last_ele)


        return "".join(temp)
                    


        
