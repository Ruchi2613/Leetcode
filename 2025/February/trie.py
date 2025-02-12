from typing import List


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        nest = self.trie
        for ch in word:
            if ch not in nest:
                nest[ch] = {}
            nest = nest[ch]
        nest["#"] = word  # Mark the end of a word

    def search(self, text: str, start: int) -> List[List[int]]:
        nest = self.trie
        result = []

        for j in range(start, len(text)):
            if text[j] not in nest:
                break
            nest = nest[text[j]]
            if "#" in nest:
                result.append([start, j])

        return result


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        result = []

        for i in range(len(text)):
            result.extend(trie.search(text, i))

        return result


# Example usage
solution = Solution()
text = "thestoryofleetcodeandme"
words = ["story", "fleet", "leetcode"]
print(solution.indexPairs(text, words))
