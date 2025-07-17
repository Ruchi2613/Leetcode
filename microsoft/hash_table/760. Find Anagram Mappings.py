class Solution:
    def anagramMappings(self, nums1, nums2):
        
        d = {}
        res = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                d[nums1[i]] = nums2.index(nums1[i])
        
        for n in nums1:
            if n in d:
                res.append(d[n])
        
        return res
cl = Solution()
print(cl.anagramMappings(nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]))