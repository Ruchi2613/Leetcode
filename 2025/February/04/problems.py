'problems of 4 and 5 February'
from collections import Counter


def word_subset(words1, words2):
    maxFreq = {}

    for word in words2:
        count = {}
        for c in word:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in count:
            if c in maxFreq:
                if count[c] > maxFreq[c]:
                    maxFreq[c] = count[c]
            else:
                maxFreq[c] = count[c]
    # print(maxFreq)
    res = []

    for x in words1:
        subset = True
        count_word1 = {}

        for wrd in x:
            if wrd not in count_word1:
                count_word1[wrd] = 1
            else:
                count_word1[wrd] += 1
        # print(count_word1)
        for key_wrd, freq_wrd in maxFreq.items():
            if key_wrd not in count_word1 or freq_wrd > count_word1[key_wrd]:
                subset = False
                break

        if subset is True:
            res.append(x)
    return res


print(word_subset(["amazon", "apple", "facebook", "google", "leetcode"], words2=["lc", "eo"]))

'''1400. Construct K Palindrome Strings'''


def canConstruct(s: str, k: int):
    if len(s) == k:
        return True

    if len(s) < k:
        return False

    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    odd = 0

    for char, freq in d.items():
        if freq % 2 == 1:
            odd += 1
            if odd > k:
                return False
    return True


print(canConstruct(s="leetcode", k=3))
'''136. Single Number'''


def singleNumber(nums):
    nu = set()

    for n in nums:
        if n in nu:
            nu.remove(n)
        else:
            nu.add(n)
    return nu.pop()


print(singleNumber(nums=[4, 1, 2, 1, 2]))

'''4.Happy Number'''


def happy_number(n):
    seen_num = set()

    while n != 1:
        sum_sqr = 0

        while n > 0:
            digit = n % 10
            sum_sqr = sum_sqr + digit * digit
            n = n // 10

        n = sum_sqr

        if sum_sqr in seen_num:
            return False
        seen_num.add(sum_sqr)

    return True
print(happy_number(n=19))


'''287. Find the Duplicate Number'''

def duplicate_number(nums):
        # d= {}

        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # print(d)

        # for k, v in d.items():
        #     print(k,v)

        #     if v >1:
        #         return k

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast
print(duplicate_number(nums=[1,3,4,2,2,4]))



