class anagram:

    def func_ana(self,s,t):
        
        d ={}
        for ch in s:
            if ch not in d:
                d[ch]= 1
            else:
                d[ch]+=1
        
        for t_ch in t:
            if t_ch not in d or t.count(t_ch)!= d[t_ch]:
                return False

        return True

cl = anagram()
print(cl.func_ana(s = "anagram", t = "nagaram"))