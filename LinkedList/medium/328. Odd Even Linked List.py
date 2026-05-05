'''328. Odd Even Linked List
Solved
Medium
Topics
conpanies icon
Companies
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore

        if head is None:
            return head
        
        odd = head
        even = odd.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = even_head

        return head

'''even ───────┐
            ▼
          [2] → [4] → None
            ▲
even_head ──┘

even = even.next   # move to 4

even ───────────► [4]

even_head ──────► [2] → [4] 


even_head is like bookmark or marker or start point


even = 2
even_head = 2

So:

even_head → 2 → 3 → 4 → 5
even       → 2 → 3 → 4 → 5

even_head → 2 → 3 → 4 → 5   (UNCHANGED)
even                 → 4 → 5'''

