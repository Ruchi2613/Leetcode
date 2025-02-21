'''1.'''
import heapq


def fillCups(amount):

    for x in range(len(amount)):
        amount[x] *= -1
    print(amount)
    heapq.heapify(amount)
    seconds = 0

    while amount[0] != 0:
        first = heapq.heappop(amount)
        second = heapq.heappop(amount)

        if second != 0:
            heapq.heappush(amount, (first + 1))
            heapq.heappush(amount, (second + 1))
        else:
            heapq.heappush(amount, (first + 1))
            heapq.heappush(amount, second)

        seconds += 1

    return seconds
print(fillCups(amount=[5,4,4]))


'''2.2231. Largest Number After Digit Swaps by Parity'''


def largestIntegar(nums):
    odd = []
    even = []
    n = str(nums)
    for x in range(len(n)):
        if int(n[x]) % 2 == 0:
            heapq.heappush(even,-int(n[x]))
        else:
            heapq.heappush(odd,-int(n[x]))
    res = []
    print(even, odd)
    for x in range(len(n)):
        if int(n[x]) % 2 == 0:
            digit = heapq.heappop(even) * -1
        else:
            digit = heapq.heappop(odd) * -1
        res.append(str(digit))
    print(res)

    return int("".join(res))

print(largestIntegar(nums=65875))


'''3.'''


def minimumOperations(nums):
    count = 0

    while True:
        min_val = float('inf')

        for num in nums:
            if num != 0 and num <= min_val:
                min_val = num

        if min_val == float('inf'):
            break

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] -= min_val

        count += 1

    return count
print(minimumOperations(nums = [1,5,0,3,5]))