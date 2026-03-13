from collections import defaultdict


class Solu:

    def countConsistentStrings(self, allowed, words):
        target_dict = defaultdict(int)

        for c in allowed:
            if c in target_dict:
                target_dict[c]+=1
            else:
                target_dict[c]=1
        # print(target_dict)
        count =0
        good = True
        for word in words:
            for letter in word:
                if letter not in target_dict:
                    good = False 
                    break
            # d = defaultdict(int)
            # for letter in word:
            #     if letter in d:
            #         d[letter]+=1
            #     else:
            #         d[letter]=1


            # good = True
            # for ch in d.keys():
            #     if ch not in target_dict:
            #         good = False
            #         break
            
            if good:
                count+=1
            

        return count
                







cl = Solu()
print(cl.countConsistentStrings(allowed = "abc", words = ["a","b","cc","ab","ac","bc","abc"]))