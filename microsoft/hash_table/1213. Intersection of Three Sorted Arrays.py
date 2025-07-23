class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        d = {}

        for x in arr1:
            if x in arr2 and x in arr3:
                d[x] = 3
        # print(d)

        if d != {}:
            return list(d.keys())
        else:
            return []
        
cl = Solution()
print(cl.arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))