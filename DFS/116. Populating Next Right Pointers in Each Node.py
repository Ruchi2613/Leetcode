'''You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from typing import Optional
from xml.dom import Node


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        #bfs:
        # q = deque()
        # q.append(root)

        # ans = []

        # if not root:
        #     return ans

        # while len(q)>0:

        #     cur_len = len(q)

        #     for x in range(cur_len):
        #         node=q.popleft()
        #         ans.append(node.val)

        #         if node.left is not None:
        #             q.append(node.left)

        #         if node.left is not None:
        #             q.append(node.left)


        #     ans.append(int('#'))

        # return ans

        # ---dfs

        if root is None:
            return None
        
        d = {}
        
        def dfs(node, depth):
            if root is None:
                return 
            if depth not in d:
                d[depth] = [node]
            else:
                d[depth].append(node)
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)

        for depth, nodes in d.items():
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
            nodes[-1].next = None
        return root
