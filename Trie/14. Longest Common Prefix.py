'''14. Longest Common Prefix
Solved
Easy
Topics
conpanies icon
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = {}

        def addWord(word):

            helper = trie
            for ch in word:
                if ch not in helper:
                    helper[ch] = {}
                helper = helper[ch]

            helper['#'] = True

        def searchPrefix(prefix, word):
            helper = trie
            new_prefix = ""
            for i in range(min(len(prefix), len(word))):
                if word[i] == prefix[i] and word[i] in helper:
                    new_prefix += word[i]
                    helper = helper[word[i]]
                else:
                    break
            
            return new_prefix
                
        addWord(strs[0])

        prefix = strs[0]

        for i in range(1, len(strs)):
            new_prefix = searchPrefix(prefix, strs[i])
            
            trie.clear()
            addWord(new_prefix)

            if new_prefix == "":
                return ""
            
        return new_prefix
