class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # dict={}
        # for i in arr:
        #     if i not in dict:
        #         dict[i]=1
        #     else:
        #         dict[i]+=1
        # count=0
        # for key,v in dict.items():
        #     if v==1:
        #         count+=1
        #         if count==k:
        #             return key
        # return "" 


        d = {}

        for x in arr:
            if arr.count(x)==1:
                d[arr.index(x)]= x

        # print(d)

        count = 0
        for ind in sorted(d.keys()):
            count+=1
            if count == k:
                return d[ind]

        return ""

            
        

        