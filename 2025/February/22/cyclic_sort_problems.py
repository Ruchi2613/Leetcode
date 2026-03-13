def cyclic_sort(n):
    for i in range(len(n)):
        correct_ind = n[i] - 1
        if correct_ind != i:
            n[i], n[correct_ind] = n[correct_ind], n[i]

    return n


print(cyclic_sort(n=[3, 1, 5, 4, 2]))

'''Find the Missing Numbers (easy)'''


def missingNumber(n):
    for i in range(len(n)):
        correct_index = n[i]
        if correct_index < len(n) and i != correct_index:
            n[i], n[correct_index] = n[correct_index], n[i]

    for i in range(len(n)):
        if n[i] != i:
            return i

    # i = 0
    # while i < len(n):
    #     correct_index = n[i]
    #     if correct_index < len(n) and n[i] != n[correct_index]:
    #         n[i], n[correct_index] = n[correct_index], n[i]  # Swap to place numbers correctly
    #     else:
    #         i += 1
    #
    # # Find the missing number
    # for i in range(len(n)):
    #     if n[i] != i:
    #         return i
    #
    # return len(n)  # If all numbers are in place, the missing number is `len(n)`


print(missingNumber(n=[3, 0, 1]))

'''448. Find All Numbers Disappeared in an Array'''


def missingNumber(nums):

    n = len(nums)

    i = 0
    while i < n:
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    # print(nums)
    res = []
    for i in range(n):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res


print(missingNumber(nums=[4,3,2,7,8,2,3,1]))


