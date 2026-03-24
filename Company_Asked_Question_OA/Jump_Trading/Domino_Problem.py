'''A domino is a rectangular tile divided into two square parts. There are between 1 and 6 dots on each of the parts.
There is an array A of length 2N, representing N dominoes. Dominoes are arranged in a line in the order in which they appear in array A. The number of dots on the left and the right parts of the Kth domino are A[2K] and A[2*K+1],respectively.
For example, an array A = [2, 4, 1, 3, 4, 6, 2, 4, 1, 6] represents a sequence of five domino tiles: (2, 4), (1, 3). (4, 6), (2, 4), and (1, 6).
In a correct domino sequence, each pair of neighbouring tiles should have the same number of dots on their adjacent parts. For example, tiles (2, 4) and (4, 6) form a correct domino sequence and tiles (2, 4) and (1, 3) do not.
What is the minimum number of domino tiles that must be removed from the sequence so that the remaining tiles form a correct domino sequence? It is not allowed to reorder or rotate the dominoes.
Write a function:
int solution(int A[ ], int M) : that, given an array A representing a sequence of N domino tiles, returns the minimum number of tiles that must be removed so that the remaining tiles form a correct domino sequence.
Examples:

Given A = [2, 4, 1, 3, 4, 6, 2, 4, 1, 6], the function should return 3. The second and
the last two dominoes should be removed. After this, the remaining dominoes are (2,4) and (4, 6).

Given A = [5, 1, 2, 6, 6, 1, 3, 1, 4, 3, 4, 3, 4, 6, 1, 2, 4, 1, 6, 2], the function should
return 7. The domino tiles that should remain are: (2, 6), (6, 1), (1, 2).

Given A = [1, 5,3, 3, 1, 3], the function should return 2. No pair of dominoes can
be connected without rotating or reordering them.

Given A = [3, 4], the function should return 0.
Write an efficient algorithm for the following assumptions:
•N is an integer within the range (1 to 50,000);
•the length of array A is equal to 2*N;
• each element of array A is an integer within the range (1 to 6)


Leetcode: https://leetcode.com/discuss/post/4014581/help-please-by-anonymous_user-5z9w/
'''


class Domino:

    def Solution(self,dom):
        
        d = {}
        res = 0
        dict_iteratorr = len(dom)//2
        # print(dict_iteratorr)
        for i in range(dict_iteratorr):
            if i not in d:
                d[i] = [dom[2*i], dom[2*i+1]]
        print(d)
        dp = [1] * dict_iteratorr
        print(dp)
        if len(dom)%2 == 0:
            for i in range(dict_iteratorr):
                left1, right1 = d[i][0], d[i][1]

                for j in range(i+1, dict_iteratorr):
                    left2, right2 = d[j][0], d[j][1]
                    
                    if right1 == left2:
                        dp[j] = max(dp[j], dp[i] + 1)
        
        res = max(dp)

        return dict_iteratorr - res


dom = Domino()
print(dom.Solution(dom= [2, 4, 1, 3, 4, 6, 2, 4, 1, 6]))

