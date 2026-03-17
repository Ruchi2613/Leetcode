'''419. Battleships in a Board
Medium
Topics
conpanies icon
Companies
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).'''


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def is_valid(r,c):
            if r < 0 or r >= row:
                return False

            if c < 0 or c>= col:
                return False

            if board[r][c] != "X":
                return False

            return True

        def dfs(r,c):
            if is_valid(r,c)== False:
                return

            board[r][c] = "F" # F as Visited(Flag)

            for add_row , add_col in directions:
                new_row = r + add_row
                new_col = c + add_col

                dfs(new_row, new_col)

        for i in range(row):
            for j in range(col):

                if board[i][j] == 'X':
                    # battle is found
                    res+=1
                    # explore all the lands connected to this island and mark them as visited
                    dfs(i,j)


        return res