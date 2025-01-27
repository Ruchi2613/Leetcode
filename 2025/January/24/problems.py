'''3423. Maximum Difference Between Adjacent Elements in a Circular Array'''


def maxAdjacentDistance(nums:int):
    n_st = nums[0]
    n_end = nums[-1]
    max_num = float('-inf')

    for i in range(len(nums) - 1):
        ele = abs(nums[i] - nums[i + 1])
        max_num = max(ele, max_num)

    return max(max_num, abs(n_end - n_st))
print(maxAdjacentDistance(nums=[1,2,4]))


def canAliceWin(n):
    stones_to_remove = 10
    alice_turn = True

    while n >= stones_to_remove:
        n = n - stones_to_remove
        stones_to_remove -= 1
        alice_turn = not alice_turn

    return not alice_turn
print(canAliceWin(n = 12))

def subarraySum(nums):
    d = {}

    for i in range(len(nums)):
        start = max(0, i - nums[i])

        d[i] = sum(nums[start:i + 1])

    print(d)

    return sum(d.values())
print(subarraySum(nums = [2,3,1]))


'''3174. Clear Digits'''


def clearDigits(s):
    res = []

    for x in s:
        if x.isdigit():
            if res:
                res.pop()
        else:
            res.append(x)
    return "".join(res)
print(clearDigits(s='acb34'))



'''1346. Check If N and Its Double Exist'''


def checkIfExist(arr):

        count = {}

        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num in arr:
            if num != 0 and 2 * num in count:
                return True
            if num == 0 and count[num] > 1:
                return True

        return False
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i != j and arr[i] == 2*arr[j]:
        #             return True
        # return False

        # d = {}

        # for x in arr:
        #     if x not in d:
        #         d[x] = 2*x

        # for val in d.values():
        #     if val in arr:
        #         return True

        # return False
print(checkIfExist(arr = [10,2,5,3]))



