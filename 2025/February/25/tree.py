import sys
from collections import deque

import null


def square_root(n):
    if (n**0.5)%1 == 0:
        return True
    else:
        return False

print(square_root(n = 49))



n = [1,2,3]

if 2 in n:
    print("hello")
if 4 in n:
    print("nope")
if 1 in n:
    print("I love you")

'''BFS'''

'''637. Average of Levels in Binary Tree'''


def averageOfLevels(root):
    q = deque()
    ans = []
    q.append(root)

    while len(q) > 0:

        cur_len = len(q)
        sum_node_val = 0

        for x in range(cur_len):
            temp = q.popleft()
            sum_node_val += temp.val

            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

        ans.append(sum_node_val / cur_len)

    return ans
print(averageOfLevels(root = [3,9,20,null,null,15,7]))

'''104. Maximum Depth of Binary Tree'''


def maxDepth(root) -> int:
    q = deque()

    q.append([root, 1])
    max_depth = -sys.maxsize

    if not root:
        return 0

    while len(q) > 0:
        child, depth = q.popleft()
        if depth > max_depth:
            max_depth = depth

        if child.left is not None:
            q.append([child.left, depth + 1])

        if child.right is not None:
            q.append([child.right, depth + 1])

    return max_depth


    # solution:

    q = deque()

    count = 0

    q.append(root)

    if not root:
        return 0

    while len(q) > 0:

        count += 1

        for x in range(len(q)):
            temp = q.popleft()

            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
                q.append(temp.right)

    return count


print(root = [3,9,20,null,null,15,7])


'''112. Path Sum'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def hasPathSum(self, root, targetSum: int) -> bool:

        if not root:
            return False

        q = deque()
        # q.append([root, 0])

        # while len(q) > 0:
        #     current_node_to_process, path_sum_before_current = q.popleft()
        #     my_own_current_value = current_node_to_process.val
        #     total_sum_with_current_value = my_own_current_value + path_sum_before_current

        #     if not current_node_to_process.left and not current_node_to_process.right and total_sum_with_current_value == targetSum:
        #         return True

        #     if current_node_to_process.left is not None:
        #         q.append([current_node_to_process.left, total_sum_with_current_value])

        #     if current_node_to_process.right is not None:
        #         q.append([current_node_to_process.right, total_sum_with_current_value])

        # return False

        q.append([root, root.val])

        while len(q) > 0:
            current_node_to_process, current_sum = q.popleft()
            if not current_node_to_process.left and not current_node_to_process.right and current_sum == targetSum:
                return True

            if current_node_to_process.left is not None:
                q.append([current_node_to_process.left, current_sum + current_node_to_process.left.val])

            if current_node_to_process.right is not None:
                q.append([current_node_to_process.right, current_sum + current_node_to_process.right.val])

        return False
print(hasPathSum(root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22))


'''965. Univalued Binary Tree'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isUnivalTree(self, root) -> bool:

        q = deque()

        q.append(root)

        while len(q) > 0:

            temp = q.popleft()

            if temp.val != root.val:
                return False

            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
                q.append(temp.right)

        return True

print(isUnivalTree(root = [2,2,2,5,2]))


'''404. Sum of Left Leaves'''


def sumOfLeftLeaves(root) -> int:
    q = deque()
    sum_val = 0
    q.append(root)

    while len(q) > 0:

        temp = q.popleft()

        if temp.left and not temp.left.left and not temp.left.right:
            sum_val += temp.left.val

        if temp.left is not None:
            q.append(temp.left)

        if temp.right is not None:
            q.append(temp.right)
    return sum_val

print(sumOfLeftLeaves(root = [3,9,20,null,null,15,7]))


''''''


def sumOfLeftLeaves(root) -> int:
    q = deque()
    sum_val = 0
    q.append(root)

    while len(q) > 0:

        current_node = q.popleft()

        left_node_of_current_node = current_node.left

        if left_node_of_current_node is not None:
            if left_node_of_current_node.left is None and left_node_of_current_node.right is None:
                sum_val += left_node_of_current_node.val

        if current_node.left is not None:
            q.append(current_node.left)

        if current_node.right is not None:
            q.append(current_node.right)

    return sum_val

#2nd solution
        q = deque()
        sum_val = 0
        q.append(root)

        while len(q) > 0:

            temp = q.popleft()

            if temp.left is not None and not temp.left.left and not temp.left.right:
                sum_val+= temp.left.val

            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
                q.append(temp.right)
        return sum_val

print(sumOfLeftLeaves(root=[3,9,20,null,null,15,7]))


''''''





