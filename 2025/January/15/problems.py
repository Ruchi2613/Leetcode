# Two Pointers
'''27. Remove Element'''


def removeElement(nums, val):
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1

    return l


print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))

'''2.977. Squares of a Sorted Array'''


def sortedSquares(nums):
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result


print(sortedSquares(nums=[-4, -1, 0, 3, 10]))


# 2nd way:

def sortedSquares(nums):
    res = []

    for x in nums:
        res.append(x ** 2)
    res = sorted(res)

    return res


print(sortedSquares(nums=[-4, -1, 0, 3, 10]))



'''3.'''


def threeSum(nums):
    res = set()
    nums.sort()

    for i in range(len(nums)):
        j = i+1
        k = len(nums)-1
        while j < k:
            valsum = nums[i] + nums[j] + nums[k]

            if valsum > 0:
                k-=1
            elif valsum < 0:
                j+=1
            else:
                res.add((nums[i], nums[j], nums[k]))
                j+=1
    res_list = []
    for x in res:
        res_list.append(x)

    return res_list

print(threeSum(nums=[-1,0,1,2,-1,-4]))

