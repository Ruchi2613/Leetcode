'''616. Add Bold Tag in String
Solved
Medium
Topics
conpanies icon
Companies
You are given a string s and an array of strings words.

You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words.

If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
If two substrings wrapped by bold tags are consecutive, you should combine them.
Return s after adding the bold tags.

 

Example 1:

Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
Explanation: The two strings of words are substrings of s as following: "abcxyz123".
We add <b> before each substring and </b> after each substring.
Example 2:

Input: s = "aaabbb", words = ["aa","b"]
Output: "<b>aaabbb</b>"
Explanation: 
"aa" appears as a substring two times: "aaabbb" and "aaabbb".
"b" appears as a substring three times: "aaabbb", "aaabbb", and "aaabbb".
We add <b> before each substring and </b> after each substring: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>".
Since the first two <b>'s overlap, we merge them: "<b>aaa</b><b>b</b><b>b</b><b>b</b>".
Since now the four <b>'s are consecutive, we merge them: "<b>aaabbb</b>".
 

Constraints:

1 <= s.length <= 1000
0 <= words.length <= 100
1 <= words[i].length <= 1000
s and words[i] consist of English letters and digits.
All the values of words are unique.
 

Note: This question is the same as 758. Bold Words in String.'''

from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        dTrie = {}

        #build Trie
        def addword(word):
            for word in words:
                helper = dTrie

                for ch in word:
                    if ch not in helper:
                        helper[ch] = {}
                    
                    helper = helper[ch]
                helper['$'] = True
        for word in words:
            addword(word)

        

        def search(start):
            helper = dTrie
            end = -1

            for i in range(start, len(s)):
                ch = s[i]

                if ch not in helper:
                    break

                helper = helper[ch]

                if "$" in helper:
                    end = i

            return end
        
        bold = [False] * len(s)

        for i in range(len(s)):
            end = search(i)

            if end != -1:
                for j in range(i, end + 1):
                    bold[j] = True


        ans = []
        i = 0

        while i < len(s):
            if bold[i] == False:
                ans.append(s[i])
                i += 1
            else:
                ans.append("<b>")
                while i < len(s) and bold[i] == True:
                    ans.append(s[i])
                    i += 1
                ans.append("</b>")

        return "".join(ans)



        



        
