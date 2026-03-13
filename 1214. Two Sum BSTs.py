# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        '''
        def dfs(curr_node, node_list):
            if not curr_node:
                return
            node_list.append(curr_node.val)
            dfs(curr_node.left, node_list)
            dfs(curr_node.right, node_list)

        node_list1, node_list2 = [], []
        dfs(root1, node_list1)
        dfs(root2, node_list2)

        # print(node_list1, node_list2)

        for i in range(len(node_list1)):
            for j in range(len(node_list2)):
                if node_list1[i] + node_list2[j] == target:
                    return True
        return False
        '''


        # Soln2:

        hash_set = set()

        q = deque()
        q.append(root1)

        while len(q)>0:
            node = q.popleft()
            hash_set.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(hash_set)


        q2 = deque()
        q2.append(root2)

        while len(q2)>0:
            node = q2.popleft()
            if (target- node.val) in hash_set:
                return True
            if node.left is not None:
                q2.append(node.left)
            if node.right is not None:
                q2.append(node.right)
        print(hash_set)

        return False