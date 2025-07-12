def containsDuplicate(nums) -> bool:
        d = {}

        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]= 1
        # print(d)

        for k,v in d.items():
            if v > 1:
                return True
        return False
print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))