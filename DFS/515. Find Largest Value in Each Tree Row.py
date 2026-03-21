'''515. Find Largest Value in Each Tree Row
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1'''


# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        depth_dict = {}

        def dfs(node, depth):
            if not node:
                return 
            
            if depth not in depth_dict:
                depth_dict[depth] = [node.val]
            else:
                depth_dict[depth].append(node.val)
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)

        # print(depth_dict)

        res = []
        maxi= -sys.maxsize

        for v in depth_dict.values():
            res.append(max(v))

        return res
            

        