class Solution:
    def sumOfUnique(self, nums) -> int:
        

        d = {}
        res = []

        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1

        print(d)

        for n , freq in d.items():
            if freq== 1:
                res.append(n)

        return sum(res)
