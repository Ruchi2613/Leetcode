class min_val:

    def func(self,list1,list2):

        res = {}
        d ={}
        ans = []

        for i in range(len(list1)):
            d[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in d:
                res[list2[j]] = j + d[list2[j]]


        min_val = min(res.values())

        for k, v in res.items():
            if v == min_val:
                ans.append(k)

        return ans


cl = min_val()
print(cl.func(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))