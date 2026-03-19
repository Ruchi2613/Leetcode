'''437. Path Sum III
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000'''

#  If you didn't understand the code please watch: https://www.youtube.com/watch?v=uZzvivFkgtM&t=468s

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prefixcount = defaultdict(int)
        prefixcount[0] = 1 # base case

        def dfs(node,currSum):
            if not node:
                return 0
            
            currSum+=node.val

            numPaths = prefixcount[currSum-targetSum]

            prefixcount[currSum]+=1

            numPaths = numPaths + dfs(node.left, currSum)
            numPaths = numPaths + dfs(node.right, currSum)

            prefixcount[currSum]-=1


            return numPaths

        return dfs(root,0)

        '''Note: prefixCount[currSum] += 1   # go down
                 prefixCount[currSum] -= 1   # backtrack
                 
                 
This line:
prefixCount[0] = 1 # BASE CASE
 Meaning:

“At the start, sum = 0 already exists once”

 Why do we need it?

So that when:

currSum == targetSum

 the path is still counted 

Example

Target = 5
Node value = 5

currSum = 5

Check:

currSum - target = 5 - 5 = 0

 Now we look at:

prefixCount[0]

If:

prefixCount[0] = 1

then:

numPaths = 1 
If this line is NOT there
prefixCount[0] = 0

 then:

numPaths = 0 

 That means we missed a valid path

-----One-line to remember

This line helps count paths that start from the root

That’s it 
If you want it even simpler or with a visual example, just tell me '''
        