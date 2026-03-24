a = [[1,2],[3,4],[5,6]]
for x in range(len(a)):
    for y in range(len(a[x])):
        print(a[x][y])


b = []
ans = [[1], [2, 3], [5, 4]]
for x in range(len(ans)):
    a = ans[x]
    b.append(a[-1])
print(b)

b = []
ans = [[1], [2, 3], [5, 4]]
for x in range(len(ans)):
    a = ans[x]
    if x % 2 != 0:
        b.append(a[::-1])
    else:
        b.append(a)
print(b)



# a = 123
# print(a[::-1])


def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for i in strs[1:]:
        while i.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(strs=["flower", "flow", "flight"]))


from typing import List
from collections import deque


