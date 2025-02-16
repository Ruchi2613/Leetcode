# '''9. Palindrome Number'''
#
# from typing import List
#
# class Trie:
#     def __init__(self):
#         self.trie = {}
#
#     def insert(self, word: str) -> None:
#         node = self.trie
#         for ch in word:
#             if ch not in node:
#                 node[ch] = {}
#             node = node[ch]
#         node["#"] = word
#
#     def search(self, strs, min_len) -> str:
#         prefix = ""
#
#         for i in range(min_len):
#             ch = strs[0][i]
#             is_common = True
#
#             for word in strs:
#                 if word[i] != ch:
#                     return prefix
#
#             if is_common:
#                 prefix += ch
#
#         return prefix
#
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         cl_trie = Trie()
#
#         for word in strs:
#             cl_trie.insert(word)
#
#         min_len = len(strs[0])
#         for word in strs:
#             if len(word) < min_len:
#                 min_len = len(word)
#
#         return cl_trie.search(strs, min_len)
#
#
# # Example usage
# sol = Solution()
# print(sol.longestCommonPrefix(["cir", "car"]))

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reverse = 0
        copy_x = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        return reverse == copy_x
obj = Solution()
print(obj.isPalindrome(x= 121))



from typing import List

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str):
        nest = self.trie
        for ch in word:
            if ch not in nest:
                nest[ch] = {}
            nest = nest[ch]
        nest["#"] = word

    def search(self, strs, min_len) -> str:
        prefix = ""
        for i in range(min_len):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return prefix
            prefix += ch
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        cl_trie = Trie()

        for word in strs:
            cl_trie.insert(word)

        min_len = len(strs[0])
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)

        return cl_trie.search(strs, min_len)


# Example usage
sol = Solution()
print(sol.longestCommonPrefix(["car", "cir"]))


'''3042. Count Prefix and Suffix Pairs I'''


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str):
        nest = self.trie
        for ch in word:
            if ch not in nest:
                nest[ch] = {}
            nest = nest[ch]
        nest["#"] = word

    def search(self,words):
        count = 0
        for i in range(len(words)):
            a = words[i]
            for j in range(i+1,len(words)):
                # print("hey:",words[j][:len(a)])
                if words[j][:len(a)] == a and words[j][-len(a):] == a:
                    count += 1

        return count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        obj_trie = Trie()

        for x in words:
            obj_trie.insert(x)

        return obj_trie.search(words)

obj = Solution()
print(obj.countPrefixSuffixPairs(words=["a","aba","ababa","aa"]))


'''3043. Find the Length of the Longest Common Prefix
'''


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

    return f'"Max_length: {max_length}"'


print(longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 4, 4]))

'2. solution:'


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, num: int):
        nest = self.trie

        str_num = str(num)
        for ch in str_num:
            if ch not in nest:
                nest[ch] = {}
            nest = nest[ch]
        nest["#"] = str_num
        print(nest)


    def search(self,num: int):
        nest = self.trie
        str_num = str(num)
        prefix_length = 0

        for ch in str_num:
            if ch in nest:
                prefix_length += 1
                nest = nest[ch]
            else:
                break
        return prefix_length
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]):
        trie_obj = Trie()

        for x in arr1:
            trie_obj.insert(x)

        max_length = 0

        for x in arr2:
            max_length = max(max_length,trie_obj.search(x))

        return max_length


obj_s = Solution()
print(obj_s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000,4]))

