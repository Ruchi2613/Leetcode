from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def create_bst(l, r):
            if l > r:
                return
            mid = l + (r - l) // 2
            node = TreeNode(nums[mid])
            print(nums[mid], l, r, mid)

            node.left = create_bst(l, mid - 1)
            node.right = create_bst(mid + 1, r)

            return node

        return create_bst(0, len(nums) - 1)


if __name__ == '__main__':
    tree = Solution()
    bst_root = tree.sortedArrayToBST([-10, -3, 0, 5, 9])
    print("Root of BST:", bst_root)

    # print(tree.sortedArrayToBST([-10,-3,0,5,9]))









