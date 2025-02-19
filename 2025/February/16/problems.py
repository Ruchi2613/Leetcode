# from typing import List
#
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.words = []
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = TrieNode()
#             node = node.children[c]
#             if len(node.words) < 3:
#                 node.words.append(word)
#
#     def prefixSearch(self, pref):
#         node = self.root
#         result = []
#         for c in pref:
#             if c not in node.children:
#                 result.extend([[]] * (len(pref) - len(result)))
#                 break
#             node = node.children[c]
#             result.append(node.words)
#         return result
#
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         trie = Trie()
#         for product in sorted(products):
#             trie.insert(product)
#         return trie.prefixSearch(searchWord)
#
#
# # Example usage
# sol = Solution()
# print(sol.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))


def solution(S):
    # Initialize variables to track first and last occurrence of 'R' and the count of 'R'
    first = -1
    last = -1
    count = 0

    for i, ch in enumerate(S):
        if ch == "R":
            count += 1
            if first == -1:
                first = i
            last = i

    # If there are no 'R's, return 0
    if first == -1:
        return 0

    # If there's only one 'R', no swaps are needed
    if first == last:
        return 0

    # Calculate the minimum swaps needed
    res = last - first - count + 1

    # If the number of swaps exceeds 10^9, return -1
    return res if res <= 10 ** 9 else -1


# Test cases
if __name__ == '__main__':
    print(solution("WRRWWR"))  # Expected: 2
    print(solution("WWRWWWRWR"))  # Expected: 4
    print(solution("WWW"))  # Expected: 0
    print(solution("RW" * 100000))  # Expected: -1
