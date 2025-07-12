class soln:

    def func(self,pattern,s):
        words = s.split()

        if len(pattern)!= len(words):
            return False
        
        d1 = {}
        d2 = {}

        for i in range(len(pattern)):

            if pattern[i] in d1:
                if d1[pattern[i]]!= words[i]:
                    return False
            else:
                d1[pattern[i]] = words[i] 


            if words[i] in d2:
                if d2[words[i]]!= pattern[i]:
                    return False
            else:
                d2[words[i]]= pattern[i]
        
        return True

cl = soln()
print(cl.func(pattern = "abba", s = "dog cat cat dog"))