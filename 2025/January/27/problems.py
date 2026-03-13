'''3063. Linked List Frequency'''
from heap1 import ListNode


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def frequenciesOfElements( head):

        temp = head
        d = {}

        while temp is not None:
            if temp.val in d:
                d[temp.val] += 1
            else:
                d[temp.val] = 1
            temp = temp.next
        # print(d)

        dict_val_list = []

        for val in d.values():
            dict_val_list.append(val)
        # print(head_val_dict)

        # new_head = head_val_dict[0]

        new_head = ListNode(dict_val_list[0])

        temp = new_head

        for x in range(1, len(dict_val_list)):
            new_node = ListNode(dict_val_list[x])
            temp.next = new_node
            temp = temp.next
        temp.next = None

        return new_head
print(frequenciesOfElements(head=[1,1,1,2,3,2]))


'''92. Reverse Linked List II'''


def reverseBetween(head, left, right):

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for l in range(left -1):
        prev = prev.next

    current = prev.next

    for x in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

print(reverseBetween(head = [1,2,3,4,5], left = 2, right = 4))


'369. Plus One Linked List'



def plusOne(head):

    reverse_list = reverse_listnode(head)

    prev = None
    cur = reverse_list
    carry = 1

    while cur is not None:
        new_val = cur.val + carry
        cur.val = new_val%10
        carry = new_val//10

        prev = cur
        curr = cur.next

    if carry:
        prev.next = ListNode(carry)

    result = reverse_list(reverse_list)

    return result

    def reverse_listnode(head):

        prev = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
