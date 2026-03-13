class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)

        cnt = 0

        for i in range(len(str_num)-k+1):
            temp = str_num[i:i+k]

            if int(temp)!= 0 and num % int(temp) == 0 :
                cnt+=1

        return cnt