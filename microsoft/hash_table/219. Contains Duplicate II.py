class conDup:

    def conDuplicates(self, nums, k):
        d = {}
        for ind, elem in enumerate(nums):
            # print(ind, elem)
            if elem in d:
                if abs(d[elem]-ind) <=k:
                    return True
            d[elem]= ind

        return False

cd= conDup()
print(cd.conDuplicates([1,2,3,1,2,3], 2))
