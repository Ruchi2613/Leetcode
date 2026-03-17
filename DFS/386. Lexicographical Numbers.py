class Solution(object):
    def lexicalOrder(self, n):

        arr = []

        for val in range(1, n+1):
            arr.append(str(val))


        print(val)

        arr.sort()
        
        res = []
        for v in arr:
            res.append(int(v))

        return res
