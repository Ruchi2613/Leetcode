from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None

            elif node.val > high:
                return dfs(node.left)

            elif node.val < low:
                return dfs(node.right)

            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        return dfs(root)

if __name__ == '__main__':
    tree = Solution()
    bst_root = tree.trimBST([-10, -3, 0, 5, 9])
    print("Root of BST:", bst_root)