class ransom:

    def func(self,ransomNote,magazine):
        
        d= {}
        for x in magazine:
            if x in d:
                d[x]+=1
            else:
                d[x]=1


        for ch in ransomNote:
            if ch in d:
                d[ch]-=1
                if d[ch] < 0:
                    return False
            else:
                return False


        return True
        # print(d)
    
cl = ransom()
print(cl.func(ransomNote = "aab", magazine = "baa"))