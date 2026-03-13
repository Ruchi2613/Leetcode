class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        res = []
        rank = 1
        arr1 = sorted(set(arr))
        for x in arr1:
            d[x] = rank
            rank+=1
        print(d)

        for num in arr:
            res.append(d[num])

        return res

        


        