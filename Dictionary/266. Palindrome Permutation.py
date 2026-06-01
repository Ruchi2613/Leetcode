'''266. Palindrome Permutation
Easy
Topics
conpanies icon
Companies
Hint
Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
235,009/342.2K
Acceptance Rate
68.7%'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        set_chr = set()

        for c in s:
            if c in set_chr:
                set_chr.remove(c)
            else:
                set_chr.add(c)
        
        return len(set_chr)<= 1