from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        pass

if __name__ == '__main__':
    tree = Solution()
    bst_root = tree.trimBST([-10, -3, 0, 5, 9])
    print("Root of BST:", bst_root)