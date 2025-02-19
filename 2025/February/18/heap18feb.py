import heapq


def kClosest(points, k):
    def euclian_formula(x, y):
        return (x ** 2 + y ** 2) ** (1 / 2)

    heap = []
    for x, y in points:
        dist = euclian_formula(x, y)
        heapq.heappush(heap, [dist, (x, y)])

    print(heap)
    res = []
    for pnts in range(k):
        closest_pnt = heapq.heappop(heap)[1]
        res.append(closest_pnt)
    return res


print(kClosest(points=[[3, 3], [5, -1], [-2, 4]]
               , k=2))

'''2. Soln'''

import heapq


def kClosest(points, k):
    def euclidean_dist(x, y):
        return (x ** 2 + y ** 2) ** (1 / 2)

    heap = []

    for x, y in points:
        dist = euclidean_dist(x, y)

        if len(heap) < k:
            heapq.heappush(heap, (-dist, x, y))
        else:
            heapq.heappushpop(heap, (-dist, x, y))
    print(heap)

    result = []
    for dist, x, y in heap:
        result.append([x, y])

    return result


print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))

'''2 Question'''


def topKFrequent(words, k: int):
    count = {}
    for y in words:
        if y in count:
            count[y] += 1
        else:
            count[y] = 1

    heap = []

    for word, freq in count.items():
        heap.append((-freq, word))
    print(heap)

    heapq.heapify(heap)

    res = []
    for x in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


'''3 question'''


# nums = [-i for i in nums]
#         heapq.heapify(nums)
#         a = heapq.heappop(nums)
#         b = heapq.heappop(nums)
#         return (abs(a)-1) * (abs(b)-1)
#
#
# def maxProduct(self, nums: List[int]) -> int:
#     for i in range(len(nums)):
#         nums[i] = -nums[i]
#     heapify(nums)
#     top_1 = -heappop(nums)
#     top_2 = -heappop(nums)
#     return (top_1 - 1) * (top_2 - 1)

def maxProduct(nums):
    for i in range(len(nums)):
        nums[i] = -nums[i]

    heapq.heapify(nums)
    print(nums)

    frst_num = heapq.heappop(nums)
    sec_num = heapq.heappop(nums)

    return (abs(frst_num) - 1) * (abs(sec_num) - 1)
    # res = []
    #
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         res.append((nums[i] - 1) * (nums[j] - 1))
    # print(res)
    # return max(res)


print(maxProduct([1, 5, 4, 5]))

'''1086. High Five'''


def high_five(items):
    d = {}

    for i in range(len(items)):
        if items[i][0] not in d:
            d[items[i][0]] = [items[i][1]]
        else:
            heapq.heappush(d[items[i][0]],items[i][1])

        if len(d[items[i][0]]) > 5:
            heapq.heappop(d[items[i][0]])

    print(d,d[1])

    res = []
    for stu_id in sorted(d.keys()):
        avg_sum = sum(d[stu_id])//5
        res.append([stu_id,avg_sum])
    return res





print(high_five(
    items=[[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
