
'''206. Reverse Linked List'''
def reverse_list(head: int):

    if head is None:
        return None

    stack = []
    temp = head

    while temp:
        stack.append(temp)
        temp = temp.next

    new_head = stack.pop()
    temp = new_head

    while stack is None:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None

    return new_head

print(reverse_list(head=[1,2,3,4,5]))

#soln 2:
    # prev = None
    # cur = head
    #
    # while cur is not None:
    #     next_node = cur.next
    #     cur.next = prev
    #     prev = cur
    #     cur = next_node
    #
    #
    # return prev


'''328. Odd Even Linked List'''

def oddEvenList(head):
    temp = head
    arr = []

    while temp is not None:
        arr.append(temp.val)
        temp = temp.next

    even = []
    odd = []

    for x in range(len(arr)):
        if x%2 == 0:
            even.append(arr[x])
        else:
            odd.append(arr[x])

    merge_even_odd = even+odd

    dummy_node = ListNode(0)
    temp = dummy_node

    for x in merge_even_odd:
        new_node = ListNode(x)
        temp.next = new_node
        temp = temp.next

    return dummy_node.next
print(oddEvenList(head = [1,2,3,4,5]))

#soln:

# if head is None:
#     return None
#
# odd_node = head
# even_node = head.next
# evenhead = head.next
#
# while odd_node.next is not None and even_node.next is not None:
#     odd_node.next = odd_node.next.next
#     even_node.next = even_node.next.next
#
#     odd_node = odd_node.next
#     even_node = even_node.next
#
# odd_node.next = evenhead




# return head

