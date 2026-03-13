
'''1708. Largest Subarray Length K'''
from collections import defaultdict


def max_subarray(nums,k):
    max_sub = []
    l = 0

    for r in range(len(nums)):
        if r-l+1 == k:
            curr_sub = nums[l:r+1]
            if max_sub is None or curr_sub > max_sub:
                max_sub = curr_sub
            l+=1
    return max_sub



print(max_subarray(nums=[1,4,5,2,3],k = 1))


'''2: 209. Minimum Size Subarray Sum'''

def min_size_subarray_sum(target, nums):

    min_len = float('inf')
    l = 0
    sum_num = 0

    for r in range(len(nums)):
        sum_num+=nums[r]
        while sum_num >= target:
        # if sum_num >= target:
            min_len = min(min_len,len(nums[l:r+1]))
            sum_num -= nums[l]
            l+=1

    if min_len == float('inf'):
        return 0
    else:
        return min_len

print(min_size_subarray_sum(target=7,nums=[2,3,1,2,4,3]))


'''3: 340. Longest Substring with At Most K Distinct Characters'''


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if k == 0:
        return 0

    max_len = 0
    l = 0
    count = defaultdict(int)

    for r in range(len(s)):
        count[s[r]] += 1
        while l < r and len(count) > k:
            if count[s[l]] == 1:
                del count[s[l]]
            else:
                count[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)

    return max_len
print(lengthOfLongestSubstringKDistinct(s = "eceba", k = 2))
