'''99. Recover Binary Search Tree
Medium
Topics
conpanies icon
Companies
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.v = []
        self.ind = 0

    def dfs_tra(self,node):
        if node is None:
            return None
        self.dfs_tra(node.left)
        self.v.append(node.val)
        self.dfs_tra(node.right)

        return
    
    def dfs_check_and_swap(self, node):
        if node is None:
            return
        
        self.dfs_check_and_swap(node.left)
        
        if self.v[self.i]!= node.val:
            node.val, self.v[self.i] = self.v[self.i], node.val

        self.i+=1
        self.dfs_check_and_swap(node.right)

        return

    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.tra(root)      # collect values
        self.v.sort()       # sort values
        self.check(root)    # place sorted values back

