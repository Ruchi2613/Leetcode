class Solution:
    def checkIfExist(self, arr):
        
        count = {}

        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        print(count)

        for num in arr:
            if num == 0 and count[num]>1:
                return True
            if num!= 0 and 2*num in count:
                return True
        return False
cl = Solution()
print(cl.checkIfExist(arr = [10,2,5,3]))