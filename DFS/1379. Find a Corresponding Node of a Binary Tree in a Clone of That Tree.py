# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """


        def __init__(self):
            self.ans = None

        def dfs(og, cloned):
            
            if og is None:
                return None
            if og == target:
                self.ans = cloned

            dfs(og.left,cloned.left)
            dfs(og.right, cloned.right)

        dfs(original,cloned)
        return self.ans