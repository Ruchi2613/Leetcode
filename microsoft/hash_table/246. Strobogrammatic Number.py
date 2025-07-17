class strobogrammatic:

    def func(self,num):

        d = {'1':'1','0':'0','8':'8','9':'6','6':'9'}
        res = []

        for x in reversed(num):
            if x not in d:
                return False
            res.append(d[x])
        
        final_res = ''.join(res)

        return final_res == num


cl = strobogrammatic()
print(cl.func(num = "69"))