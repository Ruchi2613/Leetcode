class Node:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node



class SLL:
    def __init__(self):
        self.head = None

    def append_start(self, value):
        new_node = Node(value)

        # Adding the first element
        if self.head is None:
            self.head = Node(value)

        # Adding at the start the linked list
        else:
            # new_node.next = self.head
            # self.head = new_node
            self.head = Node(value, self.head)

        self.print_linked_list("append_start")

    def delete_start(self):
        # No linked list present at the moment
        if self.head is None:
            print("Bro nothing to delete")
            return

        # Linked list exist
        second_node = self.head.next
        self.head = second_node
        self.print_linked_list("delete_start")

    def append_end(self, value):
        new_node = Node(value)

        # If linked list does not exist
        if self.head is None:
            self.head = new_node
            self.print_linked_list("append_end")
            return

        # Linked List Exists
        temp = self.head

        # Go until the last node
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        self.print_linked_list("append_end")

    def delete_end(self):

        if self.head is None:
            print("Bro nothing to delete at end")
            return

        dummy = Node(0, self.head)
        cur = dummy
        prev = dummy

        # Iterate until you reach the last node
        # Do not process last node
        while cur.next is not None:
            prev = cur
            cur = cur.next

        prev.next = None
        self.head = dummy.next

        self.print_linked_list("delete_end")

    def print_linked_list(self, name_of_operation="Nothing"):
        temp = self.head
        print(f"Printing a linked list for {name_of_operation}")
        while temp is not None:
            print(temp.key, end="\t")
            temp = temp.next
        print()


sll = SLL()

while True:
    val = input("Enter a value: ")
    if val == "x":
        break

    if " " in val:
        op, val = val.split()
    else:
        op = val

    if op == "as":
        sll.append_start(val)
    elif op == "ds":
        sll.delete_start()
    elif op == "ae":
        sll.append_end(val)
    elif op == "de":
        sll.delete_end()
