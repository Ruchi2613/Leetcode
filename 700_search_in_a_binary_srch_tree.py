# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = deque([root])

        while len(q) > 0:
            node = q.popleft()

            # if not node:
            #     return None

            if node.val == val:
                return node

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
        return None

        '''Soln 2'''
        # def searchNode(node):
        #     if node is None:
        #         return None
        #
        #     if val < node.val:  # left subtree
        #         return searchNode(node.left)
        #     elif val > node.val:  # right subtree
        #         return searchNode(node.right)
        #     elif val == node.val:
        #         return node
        #     else:
        #         return None
        #
        # return searchNode(root)