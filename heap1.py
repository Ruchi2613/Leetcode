from heapq import heappush, heappop
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = ListNode()
        tail = ans

        min_heap = []
        for i, each_node in enumerate(lists):
            if each_node is not None:
                heappush(min_heap, [each_node.val, i, each_node])

        while min_heap:
            values = heappop(min_heap)
            value = values[0]
            idx = values[1]
            node = values[2]

            tail.next = ListNode(value)
            tail = tail.next

            if node.next is not None:
                node = node.next
                heappush(min_heap, [node.val, idx, node])

        return ans.next


# Helper functions for building and printing linked lists
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(node):
    while node:
        print(node.val, end=' -> ' if node.next else '\n')
        node = node.next


# Example usage
if __name__ == "__main__":
    # Example input
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]

    # Merging the k sorted lists
    solution = Solution()
    merged_head = solution.mergeKLists(lists)

    # Print the merged linked list
    print_linked_list(merged_head)
