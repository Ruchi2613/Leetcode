'''1046. Last Stone Weight'''
import heapq
import math


def lastStoneWeight(stones):

    for x in range(len(stones)):
        stones[x] *= -1

    heapq.heapify(stones)
    print(stones)

    while len(stones) >1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)

        if stone1!=stone2:
            heapq.heappush(stones,stone1-stone2)

    if stones:
        return -heapq.heappop(stones)
    else:
        return 0
print(lastStoneWeight(stones=[2,2]))
# print(lastStoneWeight(stones=[2,7,4,1,8,1]))


'''2558. Take Gifts From the Richest Pile'''


def pickGifts(gifts, k):
    for x in range(len(gifts)):
        gifts[x] *= -1
    heapq.heapify(gifts)

    for j in range(k):
        largest = -heapq.heappop(gifts)
        rem_val = math.floor(largest ** (1 / 2)) * -1
        heapq.heappush(gifts, rem_val)

    return sum(gifts) * -1

print(pickGifts(gifts = [25,64,9,4,100], k = 4))

''''''

