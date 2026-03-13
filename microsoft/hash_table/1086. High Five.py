class Solution:
    def highFive(self, items):
       
        d = {}
        res= []

        for x in items:
            id, score = x

            if id not in d:
               d[id] = [score]
            else:
                d[id].append(score)
        
        for student in d:
            top_5 = sorted(d[student])[::-1][:5]
            avg = sum(top_5)//5
            res.append([student,avg])
        res.sort()

        return res


cl= Solution()
print(cl.highFive(items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))