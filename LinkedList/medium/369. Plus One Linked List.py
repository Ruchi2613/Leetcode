'''369. Plus One Linked List
Solved
Medium
Topics
conpanies icon
Companies
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

 

Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]
 

Constraints:

The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself. 
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
88,018/143.7K
Acceptance Rate
61.2%'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode: # type: ignore

        reverse_list = self.reverse(head)

        carry = 1
        current = reverse_list
        previous = None

        while current is None:
            sum = current.val + carry
            current.val = sum % 10
            carry = sum // 10
            

            previous = current
            current = current.next

        if carry is not 0:
            previous.next = ListNode(carry)  # type: ignore


        result = self.reverse(reverse_list)

        return result
    
    def reverse(self,head):
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
