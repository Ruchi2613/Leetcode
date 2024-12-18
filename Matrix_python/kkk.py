class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        len_list = 0

        temp = head
        while temp is not None:
            len_list += 1
            temp = temp.next
        # print(len_list)

        k_val = k % len_list
        if k_val == 0:
            return head

        start_loop = len_list - k_val

        temp = head
        for i in range(start_loop - 1):
            temp = temp.next

        first_k = temp.next
        temp.next = None

        temp = first_k
        while temp.next is not None:
            temp = temp.next

        temp.next = head

        return first_k
