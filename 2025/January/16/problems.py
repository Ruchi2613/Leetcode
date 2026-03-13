# 713. Subarray Product Less Than K
def numSubarrayProductLessThanK(nums, k):
    left = 0
    count = 0
    product = 1

    if k <= 1:
        return 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k and left <= right:
            product = product // nums[left]
            left += 1

        count += right - left + 1

    return count

print(numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))


#2.
def backspaceCompare(s: str, t: str) -> bool:
    a1 = ''
    b1 = ''

    for x in s:
        if x != '#':
            a1 += x
        else:
            a1 = a1[:-1]

    for y in t:
        if y != '#':
            b1 += y
        else:
            b1 = b1[:-1]

    if a1 == b1:
        return True
    else:
        return False

print(backspaceCompare(s = "ab#c", t = "ad#c"))


def backspaceCompare(s: str, t: str):
    def build(s):
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            else:
                ans = ans[:-1]
        return ''.join(ans)

    return build(s) == build(t)
print(backspaceCompare(s = "ab#c", t = "ad#c"))

#3.

def countGoodSubstrings(s: str) -> int:
    # k=3
    # cnt=0

    # for i in range(0,len(s)-k+1):
    #     if len(set(s[i:i+k]))==k:
    #         cnt+=1
    # return cnt

    # result = 0
    # substr = []
    # a = ''
    # k = 3

    # for x in range(len(s)):
    #     substr.append(s[x])

    #     if len(substr) > k:
    #         substr.pop(0)

    #     if len(substr) == k and len(set(substr)) == k:
    #         result += 1

    # return result

    result = []
    substrings = []

    for i in range(len(s)):
        temp = s[i: i+3]
        if len(temp) == 3:
            substrings.append(temp)

    for word in substrings:
        if len(set(word)) == len(word):
            result.append(word)

    return len(result)

print(countGoodSubstrings(s = "aababcabc"))
