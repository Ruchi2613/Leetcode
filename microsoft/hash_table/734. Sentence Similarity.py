class similarity:

    def func(self, sentence1, sentence2, similarPairs):
        d1 = {}
        d2 = {}

        for x in range(len(sentence1)):
            d1[x] = sentence1[x]

        for y in range(len(sentence2)):
            d2[y] = sentence2[y]

        if len(sentence1) != len(sentence2):
            return False
        
        for k,v in d1.items():
            if ([v,d2[k]] not in similarPairs and [d2[k],v] not in similarPairs) and (v!=d2[k]) :
                return False

        return True
    
        # soln 2:

        # if len(sentence1) != len(sentence2):
        #         return False

        # for i in range(len(sentence1)):
        #     w1 = sentence1[i]
        #     w2 = sentence2[i]

        #     if w1 == w2:
        #         continue

        #     if [w1, w2] not in similarPairs and [w2, w1] not in similarPairs:
        #         return False

        # return True


cl = similarity()
print(cl.func(sentence1 = ["great","acting","skills"],
              sentence2 = ["fine","drama","talent"],
              similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]))