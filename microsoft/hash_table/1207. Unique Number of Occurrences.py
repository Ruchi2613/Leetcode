class Solution:
    def uniqueOccurrences(self, arr):
        d = {}

        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        count_uniq = set(d.values())
        listt = list(d.values())
        # print(listt,count_uniq)

        if len(count_uniq) == len(listt):
            return True
        
        return False
    

cl = Solution()
print(cl.uniqueOccurrences(arr = [1,2,2,1,1,3]))