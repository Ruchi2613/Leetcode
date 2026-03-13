class soln:

    def func(self,jewels, stones):
        set_j = set(jewels)
        count = 0
        for st in stones:
            if st in set_j:
                count+=1
        
        return count


cl = soln()
print(cl.func(jewels = "aA", stones = "aAAbbbb"))