'''2451. Odd String Difference
Easy
Topics
conpanies icon
Companies
Hint
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

 

Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation: 
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, "abc".
Example 2:

Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
 

Constraints:

3 <= words.length <= 100
n == words[i].length
2 <= n <= 20
words[i] consists of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
45,046/72.6K
Acceptance Rate
62.0%'''

class Solution:
    def oddString(self, words: List[str]) -> str:
        # print(ord('a'))
        # print(chr(97))
        n = len(words[0])
        def diff(s):
            arr = [0]*(n-1)
            for i in range(n-1):
                arr[i] =ord(s[i+1]) - ord(s[i])
            return arr
        
        d0, d1, d2 = diff(words[0]), diff(words[1]), diff(words[2])
        
        if d0 == d1 and d1 != d2:
            return words[2]
        if d0 == d2 and d1 != d2:
            return words[1]
        if d1 == d2 and d0 != d2:
            return words[0]
        
        for i in range(3,len(words)):
            if diff(words[i]) != d0:
                return words[i]