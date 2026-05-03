'''61. Rotate List
Solved
Medium
Topics
conpanies icon
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: # type: ignore

        if head is None and k == 0:
            return head
        
        # find the length of the linked list
        n = 0
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp)
            temp = temp.next
            n += 1

        rotate = k % n

        cur_head = head

        for i in range(rotate):
            tail = stack.pop()
            tail.next = cur_head
            stack[-1].next = None
            cur_head = tail
        
        return cur_head
    

    # solution 2:

        if head is None and k == 0:
            return head
        
        # find the length of the linked list
        length = 1
        dummy = head

        while dummy.next is not None:
            dummy = dummy.next
            length += 1

        # if the list is empty or k is 0, no rotation is needed
        
        position = k % length

        if position == 0:
            return head 

        current = head
        
        for _ in range(length - position - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head
