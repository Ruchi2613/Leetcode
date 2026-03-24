from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def max_height_BST(self, root: List[int]) -> Optional[TreeNode]:

        def dfs_calc_height(node):
            if not node:
                return 0
            left_height = dfs_calc_height(node.left)
            right_height = dfs_calc_height(node.right)

            return 1 + max(left_height, right_height)

        return dfs_calc_height(root)


if __name__ == '__main__':
    tree = Solution()
    bst_root = tree.max_height_BST([-10, -3, 0, 5, 9])
    print("Root of BST:", bst_root)

    # print(tree.sortedArrayToBST([-10,-3,0,5,9]))









