class majority_element:

    def __init__(self):
        pass

    def funcx(self,nums):

        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
                count+=1
            else:
                if n == candidate:
                    count+=1
                else:
                    count-=1
        return candidate

c = majority_element()
print(c.funcx(nums=[2,2,1,1,1,2,2]))
