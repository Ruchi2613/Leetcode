'''994. Rotting Oranges
Solved
Medium
Topics
conpanies icon
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.'''


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_valid(r,c):
            if r < 0 or r >= m:
                return False
            
            if c < 0 or c >= m:
                return False
            
            if grid[r][c]!=1:
                return False
            
            return True
        
        fresh = 0
        que = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i,j))
                if grid[i][j] ==1:
                    fresh+=1

        
        if len(que) == 0 and fresh == 0:
            return 0
        

        res = -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while len(que)!=0:
            size = len(que)
            res+=1
            for i in range(size):
                p, q = que.popleft()

                for dir_p, dir_q in directions:
                    new_p = dir_p+p
                    new_q = dir_q+q
                    if is_valid(new_p, new_q) == True:
                        grid[new_p][new_q] = 2
                        fresh-=1
                        que.append((new_p,new_q))

        if fresh == 0:
            return res
        else:
            return -1


        
        

            
