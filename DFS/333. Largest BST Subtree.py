'''333. Largest BST Subtree
Medium
Topics
conpanies icon
Companies
Hint
Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.

 

Example 1:



Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.
Example 2:

Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-104 <= Node.val <= 104
 

Follow up: Can you figure out ways to solve it with O(n) time complexity?'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def isBST(node, minv, maxv):
            if node is None:
                return True
            
            if node.val <= minv or node.val >= maxv:
                return False
            
            l = isBST(node.left, minv, node.val)
            r = isBST(node.right, node.val,maxv)

            return l and r 

        def cal_size(node):
            if node is None:
                return 0

            return 1+ cal_size(node.left)+ cal_size(node.right) 
        
        if isBST(root, float('-inf'), float('inf')) == True:
            return cal_size(root)
        
        return max(self.largestBSTSubtree(root.left),
                   self.largestBSTSubtree(root.right))
