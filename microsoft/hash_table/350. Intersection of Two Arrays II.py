class twoArray:

    def func(self,nums1,nums2):
        
        d1 = {}
        d2 = {}
        res = []

        for x in nums1:
            if x in d1:
                d1[x]+=1
            else:
                d1[x] = 1

        for y in nums2:
            if y in d2:
                d2[y]+=1
            else:
                d2[y]= 1
        
        for k in d1.keys()&d2.keys():
            res.extend([k]*min(d1[k],d2[k]))

        return res
cl = twoArray()
print(cl.func(nums1 = [1,2,2,1], nums2 = [2,2]))