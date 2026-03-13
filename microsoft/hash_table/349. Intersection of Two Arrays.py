class intersection:

    def func(self,nums1,nums2):
        # res = set()

        # for x in nums1:
        #     if x in nums2:
        #         res.add(x)

        # return list(res)


        d = {}
        res = []

        for x in nums1:
            d[x] = 1

        for y in nums2:
            if y in d and d[y]==1:
                d[y] = 0
                res.append(y)
        return res
            
cl = intersection()
print(cl.func(nums1 = [1,2,2,1], nums2 = [2,2]))