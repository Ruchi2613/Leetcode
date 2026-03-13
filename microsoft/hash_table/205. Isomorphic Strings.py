def isIsomorphic(s: str, t: str) -> bool:
    d1 = {}
    d2 = {}


    for i in range(len(s)): 
        
        # s string
        if s[i] in d1:
            if d1[s[i]]!= t[i]:
                return False
        else:
            d1[s[i]] = t[i]

        # t string

        if t[i] in d2:
            if d2[t[i]]!= s[i]:
                return False
        else:
            d2[t[i]] = s[i]
    print(d1,d2)
    return True

print(isIsomorphic(s = "foo", t = "bar"))


        

