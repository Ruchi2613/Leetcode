# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}

        def dfs(node):
            if node is None:
                return

            if node.val in d:
                d[node.val]+=1
            else:
                d[node.val]=1

            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)

        print(d)

        k_node_list = list()
        maxi_val= max(d.values())
        # print(maxi_val)

        for k, val in d.items():
            if val == maxi_val:
                k_node_list.append(k)
        return k_node_list

        # editorial 1 soln:
        #
        # def dfs(node, counter):
        #
        #     if node is None:
        #         return
        #
        #     counter[node.val] += 1
        #     dfs(node.left, counter)
        #     dfs(node.right, counter)
        #
        # counter = defaultdict(int)
        # dfs(root, counter)
        # max_freq = max(counter.values())
        #
        # ans = []
        # for key in counter:
        #     if counter[key] == max_freq:
        #         ans.append(key)
        # return ans

        '''editorial soln 2: Deque(BFS)'''

        # counter = defaultdict(int)
        # queue = deque([root])
        #
        # while queue:
        #     node = queue.popleft()
        #     counter[node.val] += 1
        #
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        #
        # max_freq = max(counter.values())
        #
        # ans = []
        # for key in counter:
        #     if counter[key] == max_freq:
        #         ans.append(key)
        #
        # return ans

        '''editorial soln 3'''

        # counter = defaultdict(int)
        # stack = [root]
        #
        # while stack:
        #     node = stack.pop()
        #     counter[node.val] += 1
        #
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        #
        # max_freq = max(counter.values())
        #
        # ans = []
        # for key in counter:
        #     if counter[key] == max_freq:
        #         ans.append(key)
        #
        # return ans


