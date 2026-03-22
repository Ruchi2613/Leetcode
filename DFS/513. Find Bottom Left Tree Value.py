'''513. Find Bottom Left Tree Value
Solved
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth_dict = {}

        def dfs(node, depth):
            if node is None:
                return 
            
            if depth not in depth_dict:
                depth_dict[depth] = [node.val]
            else:
                depth_dict[depth].append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)

        # get max depth
        max_depth = max(depth_dict.keys())

        return depth_dict[max_depth][0]
        # for v in reversed(depth_dict.values()):
        #     return v[0]
            


        