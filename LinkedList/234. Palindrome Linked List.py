'''234. Palindrome Linked List
Solved
Easy
Topics
conpanies icon
Companies
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # solution 1: using list 
        temp = head
        local_lst = []

        while temp is not None:
            local_lst.append(temp.val)
            temp = temp.next
        
        return local_lst == local_lst[::-1]
    
        # solution 2: using stack
        temp = head
        stack = []

        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head
        while temp is not None:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        
        return True
    
    