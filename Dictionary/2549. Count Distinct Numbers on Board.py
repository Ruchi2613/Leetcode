'''2549. Count Distinct Numbers on Board
Easy
Topics
conpanies icon
Companies
Hint
You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
Then, place those numbers on the board.
Return the number of distinct integers present on the board after 109 days have elapsed.

Note:

Once a number is placed on the board, it will remain on it until the end.
% stands for the modulo operation. For example, 14 % 3 is 2.
 

Example 1:

Input: n = 5
Output: 4
Explanation: Initially, 5 is present on the board. 
The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. 
After that day, 3 will be added to the board because 4 % 3 == 1. 
At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5. 
Example 2:

Input: n = 3
Output: 2
Explanation: 
Since 3 % 2 == 1, 2 will be added to the board. 
After a billion days, the only two distinct numbers on the board are 2 and 3. 
 

Constraints:

1 <= n <= 100'''

class Solution:
    def distinctIntegers(self, n: int) -> int:
        # The numbers on the board will be all the integers from 2 to n, inclusive.
        # This is because for any integer x > 1, there will always be an integer i such that x % i == 1 (specifically, i = x - 1).
        # For n = 1, the only number on the board is 1 itself, so the count of distinct integers is 1.
        # For n > 1, the distinct integers on the board will be 2, 3, ..., n, which gives us a total of n - 1 distinct integers.
        # solution is O(1) time complexity and O(1) space complexity.
        '''if n == 1:
            return 1
        
        return n-1'''


        board = {n}

        change = True

        while change == True:
            change = False
            new_board = set()

            for x in board:
                for i in range(1, n+1):
                    if x % i == 1 and i not in board:
                        new_board.add(i)
                        change = True
            
            board.update(new_board)
        
        return len(board)