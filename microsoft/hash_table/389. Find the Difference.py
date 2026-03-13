class diff:

    def func(self,a,b):
        d = {}

        for x in a:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        # print(d)

        for y in b:
            if y not in d or d[y]==0:
                return y
            else:
                d[y]-=1

d = diff()
print(d.func(a= 'a',b = 'aa'))