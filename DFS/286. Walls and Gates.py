'''286. Walls and Gates
Medium
Topics
conpanies icon
Companies
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]'''

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """


        m = len(rooms)
        n = len(rooms[0])
        
        def is_valid(x,y):

            if x < 0 or x >= m:
                return False
            if y < 0 or y >= n:
                return False
            if rooms[x][y] != 2147483647:
                return False
            return True

        que = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    que.append((i,j,0)) # r,c, distance

        directions_neighbors= [[1,0],[-1,0],[0,1],[0,-1]]
        while len(que)>0:
            size = len(que)
            
            for i in range(size):
                r, c , distance = que.popleft()

                for dir_r, dir_c in directions_neighbors:
                    new_r = dir_r+r
                    new_c = dir_c+c

                    if is_valid(new_r,new_c) == True:
                        rooms[new_r][new_c] = distance + 1 
                        que.append((new_r, new_c, distance + 1))
        