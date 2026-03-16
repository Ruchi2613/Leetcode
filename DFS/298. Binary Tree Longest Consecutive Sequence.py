'''298. Binary Tree Longest Consecutive Sequence
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by one along the path.

Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

 

Example 1:


Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:


Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def longestConsecutive(self, root):
        self.res = 0
        
        def dfs(node, parent, length): # (current, prev , consecutive len)
            if not node:
                return None
            
            if parent is not None and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            
            self.res = max(self.res, length)
            
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, None, 0)
        return self.res