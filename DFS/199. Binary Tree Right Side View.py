'''199. Binary Tree Right Side View
Solved
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.d = {}
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
  
        def dfs(node,depth):
            if not node:
                return 
            
            if depth not in self.d:
                self.d[depth] = [node.val]
            else:
                self.d[depth].append(node.val)

            dfs(node.left,depth+1)
            dfs(node.right, depth+1)
        

        dfs(root,1)
        ans = []

        for k,v in self.d.items():
            ans.append(v[-1])

        return ans

        


        # if not root: return []

        # queue = deque([root])
        # result = []

        # while queue:
        #     size = len(queue)

        #     for i in range(size):
        #         node = queue.popleft()
        #         if i == size - 1:
        #             result.append(node.val)

        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)

        # return result


        # if not root:
        #     return []

        # q = deque()
        # q.append(root)
        # ans = []
        
        # while len(q)>0:

        #     inner_list = []
        #     curr_len = len(q)

        #     for x in range(curr_len):
        #         temp = q.popleft()

        #         inner_list.append(temp.val)

        #         if temp.left is not None:
        #             q.append(temp.left)
        #         if temp.right is not None:
        #             q.append(temp.right)
                
        #     ans.append(inner_list)

        # final_list = []
        # for x in ans:
        #     # a = x[-1]
        #     final_list.append(x[-1])
        # return final_list
