import heapq


def topKFrequent(words, k):
    count = {}
    for y in words:
        if y in count:
            count[y]+=1
        else:
            count[y] =1

    heap = []

    for word, freq in count.items():
        heap.append((-freq, word))

    heapq.heapify(heap)

    result = []
    for x in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))



# # import heapq
# #
# # heap_l = [-1,0,-1,-1,3,4]
# # heapq.heapify(heap_l)
# # print(heap_l)
# # def solution(S):
# #     positions = [i for i, c in enumerate(S) if c == 'R']
# #     RCount = len(positions)
# #
# #     if RCount == 0:
# #         return 0  # No red balls to move
# #
# #     mid = RCount // 2
# #     median = positions[mid]  # Median position of R's
# #
# #     swaps = sum(abs(pos - (median - (mid - i))) for i, pos in enumerate(positions))
# #
# #     return swaps if swaps <= 10**9 else -1
# #
# #
# # if __name__ == '__main__':
# #     print(solution("WRRWWR"))  # Output: 2
# #     print(solution("WWRWWWRWR"))  # Output: 4
# #     print(solution("WWW"))  # Output: 0
# #     print(solution("RW" * 100000))  # Output: -1
#
#
# # def minSwaps(s):
# #     rtn = 0
# #     RCount = 0
# #     if 'R' not in s:
# #         return 0
# #     first = s.index('R')
# #     for i in range(0, len(s)):
# #         if s[i] == 'R':
# #             RCount +=1
# #             rtn = i
# #     # print(rtn,first,RCount)
# #     if rtn == first:
# #         return 0
# #     else :
# #         return rtn-first-RCount+1
# #
# #
# #
# # if __name__ == '__main__':
# #      s= "RW"
# #      print(minSwaps(s))
#
#
# def min_adj_swap_red_balls(s: str) -> int:
#      red_index = [i for i, ch in enumerate(s) if ch == 'R']
#      res = 0
#      mid = len(red_index) // 2
#      for i in range(len(red_index)):
#          res += abs(red_index[mid] - red_index[i]) - abs(mid - i)
#      return res
#
# print(min_adj_swap_red_balls(s= "RW"))
#
#
#
