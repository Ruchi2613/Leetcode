'''863. All Nodes Distance K in Binary Tree
Solved
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000'''


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.parent = {}

        def addParent(self, node):
            if node is  None:
                return None
            
            if node.left is not None:
                self.parent[node.left] = node
                self.addParent(node.left)

            if node.right is not None:
                self.parent[node.right] = node
                self.addParent(node.right)

        def collectKDistanceNodes(self, target, k, result):

            q = deque([target])
            visited = set([target])

            while len(q)>0:
                size = len(q)

                if k == 0:
                    for node in q:
                        result.append(node.val)
                    return
                
                for i in range(size):
                    node = q.popleft()

                    if node.left is not None and node.left not in visited:
                        visited.add(node.left)
                        q.append(node.left)

                    if node.right is not None and node.right not in visited:
                        visited.add(node.right)
                        q.append(node.right)

                    if node in self.parent and self.parent[node] not in visited:
                        visited.add(self.parent[node])
                        q.append(self.parent[node])

            k-=1

        def distanceK(self, root, target, k):
            result = []
            self.addParent(root)
            self.collectKDistanceNodes(target, k, result)
            return result


