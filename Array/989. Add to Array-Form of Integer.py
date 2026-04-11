'''The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104'''

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        n1 = ''
        for s in num:
            n1 = n1 + str(s)

        n2 = str(k)

        def cal_sum(n1, n2):
            i = len(n1) - 1
            j = len(n2) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry != 0:

                if i >= 0:
                    d1 = int(n1[i])
                else:
                    d1 = 0

                if j >= 0:
                    d2 = int(n2[j])
                else:
                    d2 = 0

                total = d1 + d2 + carry

                digit = total % 10
                carry = total // 10

                res.append(digit)

                i = i - 1
                j = j - 1

            # result = []
            # idx = len(res) - 1

            # rev = reversed(res)
            # print(rev)
            # while idx >= 0:
            #     result.append(res[idx])
            #     idx = idx - 1

            return res[::-1]

        return cal_sum(n1, n2)