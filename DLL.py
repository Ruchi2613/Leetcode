class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DLL:

    def __init__(self):
        self.head = None
        self.length = 0

    def add_at_head(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node

        else:
            new_node.right = self.head
            self.head = new_node
        self.length += 1

    def delete_at_head(self):

        if self.length == 0:
            print("no Node exist")

        else:
            self.head = self.head.next

        self.length -= 1

    def add_at_tail(self, val):

        new_node = Node(val)

        temp = self.head

        while temp.right is not None:
            temp = temp.right

        temp.right = new_node
        new_node.left = temp

        self.length += 1

    def delete_at_tail(self):
        if self.length == 0:
            print("no Node exist")

        if self.length == 1:
            self.head = None

        else:
            temp = self.head
            while temp.right is not None:
                temp = temp.right

            second_last_node = temp.left
            second_last_node.right = None
        self.length -= 1
