# Definition for a binary tree node.
import sys
'''it will run on Leetcode'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        # closest = root.val
        # while root:
        #     closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
        #     root = root.left if target < root.val else root.right
        # return closest

        diff = 0
        closest = sys.maxsize
        node_nearest = root.val

        def nearest(node):
            nonlocal diff, closest, node_nearest
            if node is None:
                return

            diff = abs(node.val - target)

            if diff < closest:
                closest = diff
                node_nearest = node.val

            elif diff == closest:
                closest = diff
                node_nearest = min(node.val, node_nearest)

            if target < node.val:
                nearest(node.left)
            else:
                nearest(node.right)

        nearest(root)
        return node_nearest


if __name__ == '__main__':
    tree = Solution()
    bst_root = tree.closestValue(root = [4,2,5,1,3], target = 3.714286)

    print("Root of BST:", bst_root)

