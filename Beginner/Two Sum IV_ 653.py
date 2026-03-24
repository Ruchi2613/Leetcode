# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        '''Soln 1'''
        # nodeValues = []

        # def dfs(node):
        #     if node is None:
        #         return
        #     nodeValues.append(node.val)

        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)

        # print(nodeValues)
        # sum_num = 0
        # for i in range(len(nodeValues)):
        #     for j in range(i+1,len(nodeValues)):
        #         if nodeValues[i]+nodeValues[j] == k:
        #             return True

        # return False

        '''Editorial soln 2'''
        # seen = set()
        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     if(k - node.val in seen):
        #         return True
        #     else:
        #         seen.add(node.val)
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return False

        '''Editorial soln 3'''


        def dfs(root,sett):
            if not root:
                return False

            if abs(k-root.val) in sett:
                return True
            else:
                sett.add(root.val)

            left = dfs(root.left, sett)
            right = dfs(root.right, sett)

            return left or right
        sett = set()
        return dfs(root,sett)





