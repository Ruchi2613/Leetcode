from collections import Counter, defaultdict

class Solution:
    def maxNumberOfBalloons(self,text):
        main_dict = Counter("balloon")

        count_res = 0
        dict_t = defaultdict(int)
        for ch in text:
            if ch in main_dict:
                if ch in dict_t:
                    dict_t[ch]+=1
                else:
                    dict_t[ch]=1 
        # print(d1,main_dict)

        while True:

            good = True
            for ch, freq in main_dict.items():
                count_left = dict_t[ch]

                if count_left < freq:
                    good = False
                    break
                dict_t[ch]-=freq

            if good:
                count_res+=1
            else:
                break

        return count_res
    
cl = Solution()
print(cl.maxNumberOfBalloons(text='loonbalxballpoon'))