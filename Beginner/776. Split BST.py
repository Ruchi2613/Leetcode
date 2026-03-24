# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: Optional[TreeNode], V: int) -> List[Optional[TreeNode]]:

        def dfs(root, V):
            if not root:
                return []

            if root.val <= V:
                # root belongs to the left tree
                leftSubtree, rightSubtree = dfs(root.right, V)
                root.right = leftSubtree
                return (root, rightSubtree)
            else:
                # root belongs to the right tree
                leftSubtree, rightSubtree = dfs(root.left, V)
                root.left = rightSubtree
                return (leftSubtree, root)
        return dfs(root,V)


