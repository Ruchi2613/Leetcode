class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        one = zero = 0
        l = 0

        for r in range(len(s)):
            if s[r] == '1':
                one+=1
            else:
                zero+=1


            while one > k and zero > k:
                if s[l] == '1':
                    one-=1
                else:
                    zero-=1

                l+=1

            res+=r-l+1

        return res
    

        '''brute force'''

        '''
        for l in range(len(s)):
            zero = one = 0

            for r in range(l,len(s)):
                if s[r] == '1':
                    one+=1
                else:
                    zero+=1

                if one <= k or zero <= :
                    res+=1

                else:
                    break

            return res          
        
        
        '''
