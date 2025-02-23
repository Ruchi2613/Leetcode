'''3264. Final Array State After K Multiplication Operations I'''
import heapq


def getFinalState(nums, k, multiplier):
    '''sol 1:'''
    # while k > 0:
    #     min_val = float('inf')
    #     ind = 0
    #
    #     for x in range(len(nums)):
    #         if nums[x] < min_val:
    #             min_val = nums[x]
    #             ind = x
    #
    #     for i in range(len(nums)):
    #         if i == ind:
    #             nums[i] *= multiplier
    #             k -= 1
    #
    # return nums

    '''Sol 2:'''
    heap = []
    for ind, n in enumerate(nums):
        heap.append((n, ind))

    heapq.heapify(heap)
    print(heap)

    while k > 0:
        min_val,ind = heapq.heappop(heap)
        nums[ind] *= multiplier
        heapq.heappush(heap, (nums[ind], ind))
        k -= 1
    return nums


print(getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))

'''506. Relative Ranks'''


def findRelativeRanks(score):
    heap = []
    n = len(score)

    for ind, score in enumerate(score):
        heapq.heappush(heap, (-score, ind))
    print(heap)

    rank = [0] * n
    place = 1
    while heap:
        original_index = heapq.heappop(heap)[1]
        # print(original_index)

        if place == 1:
            rank[original_index] = "Gold Medal"
        elif place == 2:
            rank[original_index] = "Silver Medal"
        elif place == 3:
            rank[original_index] = "Bronze Medal"
        else:
            rank[original_index] = str(place)
        place += 1
    return rank
print(findRelativeRanks(score = [5,4,3,2,1]))


''''''