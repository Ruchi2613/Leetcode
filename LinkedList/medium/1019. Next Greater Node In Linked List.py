# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        temp_list = []

        temp = head

        while temp is not None:
            temp_list.append(temp.val)
            temp = temp.next


        res = [0]* len(temp_list)

        stack = []

        for i in range(len(temp_list)):

            while stack and temp_list[stack[-1]] < temp_list[i]:
                # res[stack.pop()] = temp_list[i]
                smaller_index = stack.pop()
                res[smaller_index] = temp_list[i]
            stack.append(i)

        return res
