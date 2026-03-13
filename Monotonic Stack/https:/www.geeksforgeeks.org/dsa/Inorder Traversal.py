from typing import Optional, List

from Leetcode.min_height_of_BST import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        if root == None:
            return elements
        itr = root
        # first we get all left elements
        if itr.left is not None:
            elements = elements + self.inorderTraversal(itr.left)
        # print root
        elements.append(itr.val)

        if itr.right is not None:
            elements = elements + self.inorderTraversal(itr.right)

        return elements