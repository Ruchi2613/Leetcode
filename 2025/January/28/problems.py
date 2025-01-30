'237. Delete Node in a Linked List'


def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """

    node.val = node.next.val
    node.next = node.next.next


'1836. Remove Duplicates From an Unsorted Linked List'


def deleteDuplicatesUnsorted(head):
    d = {}

    dummy = ListNode(-1,head)
    current = head

    while current is not None:
        if current.val in d:
            d[current.val]+=1
        else:
            d[current.val] = 1

        current = current.next

    current = dummy
    while current.next is not None:
        if current.val == 1:
            current = current.next
        else:
            current.next = current.next.next
    return dummy.next

'''3217. Delete Nodes From Linked List Present in Array'''

def modifiedList(nums, head):
    num_set = set(nums)
    dummy = ListNode(-1, head)
    cur = dummy

    while cur and cur.next is not None:
        if cur.next.val in num_set:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


print(modifiedList(nums = [1,2,3], head = [1,2,3,4,5]))


'''141. Linked List Cycle'''
def hasCycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

    # node_set = set()

    # current = head

    # while current is not None:
    #     if current in node_set:
    #         return True
    #     node_set.add(current)
    #     current = current.next
    # return False

'resume update'
'old project fixing'
'microsoft setup doc'

