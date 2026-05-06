'''445. Add Two Numbers II
Solved
Medium
Topics
conpanies icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
581,535/928.9K
Acceptance Rate
62.6%'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def helper(a1,a2):
        stack1 = []
        stack2 = []

        while a1 is not None:
            stack1.append(a1.val)
            a1 = a1.next

        while a2 is not None:
            stack2.append(a2.val)
            a2 = a2.next

        carry = 0
        res = None


        while stack1 or stack2 or carry:
            
            if stack1 is not None:
                digit1 = stack1.pop()
            else:
                digit1 = 0

            if stack2 is not None:
                digit2 = stack2.pop()
            else:
                digit2 = 0
        
            total_sum = digit1 + digit2 + carry
            node = total_sum % 10
            carry = total_sum // 10

            new_node = ListNode(node)  # type: ignore
            new_node.next = res
            res = new_node

        return res



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        ans = self.helper(l1, l2)
        return ans



    
        
