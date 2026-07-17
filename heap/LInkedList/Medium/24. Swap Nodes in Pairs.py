'''24. Swap Nodes in Pairs
Solved
Medium
Topics
conpanies icon
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Beginner.heap1 import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        even = head
        ans = ListNode(0)
        temp = ans


        while even is not None and even.next is not None:
            odd = even.next

            temp.next = ListNode(odd.val)
            temp = temp.next
            temp.next = ListNode(even.val)
            temp = temp.next

            even = odd.next

        if even is not None:
            temp.next = ListNode(even.val)

        return ans.next
