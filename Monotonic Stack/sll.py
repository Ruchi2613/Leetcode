class Node:

    def __init__(self, val, next_node=None):
        self.value = val
        self.next = next_node


class SLL:

    def __init__(self):
        self.head = None

    def append_start(self, value):

        if self.head is None:
            self.head = Node(value)

        else:
            self.head = Node(value, self.head)
        self.print_linked_list("append_start")

    def delete_start(self):
        if self.head is None:
            print("nothing to delete")
            return
        else:
            second_node = self.head.next
            self.head = second_node
        self.print_linked_list("delete_start")

    def append_end(self, value):

        if self.head is None:
            self.head = Node(value)
            return
        else:

            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(value)
            self.print_linked_list("append_start")
    def delete_end(self):

        if self.head is None:
            print("Bro nothing to delete at end")
            return

        # dummy = Node(0, self.head)
        # cur = dummy
        # prev = dummy
        temp = self.head

        while temp.next.next is not None:
            temp = temp.next
            
        temp.next = None
        self.print_linked_list("delete_end")

    def print_linked_list(self, name_of_operation="Nothing"):
        temp = self.head
        print(f"Printing a linked list for {name_of_operation}")
        while temp is not None:
            print(temp.value, end="\t")
            temp = temp.next
        print()

sll = SLL()
while True:
    val = input("Enter a value: ")
    if val == "x":
        break

    parts = val.split()

    if len(parts) == 1:  # Handles commands like "ds" or "de"
        op = parts[0]
        val = None
    else:
        op, val = parts

    if op == "as":
        sll.append_start(val)
    elif op == "ds":
        sll.delete_start()
    elif op == "ae":
        sll.append_end(val)
    elif op == "de":
        sll.delete_end()