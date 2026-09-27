'''345. Reverse Vowels of a String
Solved
Easy
Topics
conpanies icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelset = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        i = 0
        j = len(s)-1

        while i <j:

            if s_list[i] in vowelset and s_list[j] in vowelset:
                s_list[i],s_list[j] = s_list[j],s_list[i]
                i+=1
                j-=1

            elif s_list[i] in vowelset and s_list[j] not in vowelset:
                j-=1
            else:
                i+=1

        return ''.join(s_list)