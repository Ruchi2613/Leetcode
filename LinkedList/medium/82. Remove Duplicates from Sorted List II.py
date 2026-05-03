'''82. Remove Duplicates from Sorted List II
Solved
Medium
Topics
conpanies icon
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:   # type: ignore

        listt = []
        d = {}

        temp = head

        while temp is not None:
            listt.append(temp.val)
            temp = temp.next

        for ele in listt:
            if ele in d:
                d[ele]+=1
            else:
                d[ele] =1
        
        ans = []
        for k, v in d.items():
            if v == 1:
                ans.append(k)
        
        temp = ListNode(0)
        dummy = temp
        
        for x in ans:
            dummy.next = ListNode(x)
            dummy = dummy.next

        return temp.next


