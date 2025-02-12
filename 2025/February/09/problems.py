from typing import List

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = word

    def search(self, s: str, start: int) -> bool:
        node = self.trie

        for j in range(start, len(s)):
            ch = s[j]
            if ch not in node:
                return False
            node = node[ch]
            if "#" in node:
                if self.search(s, j + 1):
                    return True
        return "#" in node

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        return trie.search(s, 0)

solution = Solution()

s = "leetcode"
wordDict = ["leet", "code"]
print(solution.wordBreak(s, wordDict))