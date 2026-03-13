# '''1422. Maximum Score After Splitting a String'''
#
#
# class Solution:
#     def maxScore(self, s: str) -> int:
#
#         ones = s.count("1")
#         zeros = 0
#         ans = 0
#
#         for i in range(len(s) - 1):
#             if s[i] == "1":
#                 ones -= 1
#             else:
#                 zeros += 1
#
#             ans = max(ans, zeros + ones)
#
#         return ans
#     # sol: 1
#
#     # sol: 2
#     # ans = 0
#
#     # for i in range(len(s)-1):
#     #     curr = 0
#
#     #     for j in range(i+1):
#     #         if s[j] == "0":
#     #             curr+=1
#
#     #     for j in range(i+1,len(s)):
#     #         if s[j] == "1":
#     #             curr+=1
#
#     #     ans = max(ans, curr)
#
#     # return ans
#
#     # sol: 3
#
#     # nums = list(s)
#
#     # maxi = 0
#     # print(nums)
#     # for i in range(len(nums)-1):
#     #     count_1 = 0
#     #     count_0 = 0
#
#     #     for j in range(i+1):
#     #         if s[j] == '0':
#     #             count_0 +=1
#
#     #     for j in range(i+1,len(nums)):
#     #         if s[j] == '1':
#     #             count_1 +=1
#
#     #     maxi = max(maxi, count_0 + count_1)
#     # return maxi
#
#
# '''2559. Count Vowel Strings in Ranges'''
#
#
# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         # ans = []
#
#         # for query in queries:
#         #     count = 0
#         #     start, end = query
#
#         #     for i in range(start, end + 1):
#         #         if words[i][0] in vowels and words[i][-1] in vowels:
#         #             count += 1
#
#         #     ans.append(count)
#
#         # return ans
#
#         n = len(words)
#
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i]
#             if words[i][0] in vowels and words[i][-1] in vowels:
#                 prefix[i + 1] += 1
#
#         ans = []
#         for start, end in queries:
#             ans.append(prefix[end + 1] - prefix[start])
#
#         return ans
#
#
# '''2270. Number of Ways to Split Array'''
#
#
# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#
#         # left_sum = 0
#
#         # right_sum = sum(nums)
#         # count = 0
#
#         # for i in range(len(nums)-1):
#         #     left_sum+=nums[i]
#         #     right_sum-=nums[i]
#
#         #     if left_sum>=right_sum:
#         #         count+=1
#
#         # return count
#
#         # count = 0
#
#         # for i in range(len(nums)-1):
#         #     left,right = 0,0
#
#         #     for j in range(i+1):
#         #         left+=nums[j]
#
#         #     for j in range(i+1,len(nums)):
#         #         right+=nums[j]
#
#         #     if left >= right:
#         #         count+=1
#
#         # return count
#
#         count = 0
#
#         for i in range(len(nums) - 1):
#             if sum(nums[:i + 1]) >= sum(nums[i + 1:]):
#                 count += 1
#         return count
#
#
# '''2185. Counting Words With a Given Prefix'''
#
#
# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#
#         count = 0
#
#         for i in range(len(words)):
#             a = ''
#             a += words[i]
#             # print(a[:len(pref)])
#
#             if a[:len(pref)] == pref:
#                 count += 1
#             elif len(a) > len(pref):
#                 continue
#
#         return count

# x = 123
# s = str(x)
# print(s[::-1])

a = 'ruchi'
print("hello:",a[:3])
x = ['ruchi','2222']
i = 2
for j in range(len(x)):
    print(x[j][i])

    from typing import List


    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False


    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word: str):
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        def longest_prefix(self, word: str) -> int:
            node = self.root
            length = 0
            for ch in word:
                if ch in node.children:
                    length += 1
                    node = node.children[ch]
                else:
                    break
            return length


    class Solution:
        def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
            trie = Trie()

            # Insert all numbers from arr1 into the Trie
            for num in arr1:
                trie.insert(str(num))

            max_length = 0

            # Find the longest prefix match in arr2
            for num in arr2:
                max_length = max(max_length, trie.longest_prefix(str(num)))

            return max_length


from typing import List

def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}

        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    prefix_map[prefix] += 1
                else:
                    prefix_map[prefix] = 1

        max_length = 0

        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in prefix_map:
                    if len(prefix) > max_length:
                        max_length = len(prefix)

        return max_length
print(longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]))
