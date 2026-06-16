
# __lt__ function is used to compare two objects of a class. It is called when the < operator is used to compare two objects of a class. The __lt__ function should return True if the object on the left side of the < operator is less than the object on the right side, and False otherwise.
class Box:
    def __init__(self, value):
        self.value = value

    def __lt__(self, B):
        return self.value < B.value
    

A = Box(5)
B = Box(10)

print(A < B)  # True
print(B < A)  # False


# with ListNode

class ListNode:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next

class HeapNode:
    def __init__(self,node):
        self.node = node

    def __lt__(self, B):
        return self.node.val < B.node.val

    
node1 = ListNode(5)
node2 = ListNode(10)

A = HeapNode(node1)
B = HeapNode(node2)

print(A < B)  # True
print(B < A)  # False

'''Step 1
node1 = ListNode(3)

Python calls:

node1.__init__(3)

Inside:

self = node1
val = 3

So:

self.val = val

becomes:

node1.val = 3
Step 2
A = HeapNode(node1)

Python calls:

A.__init__(node1)

Inside:

self = A
node = node1

So:

self.node = node

becomes:

A.node = node1

Now A stores a reference to node1.

Memory:

A
 └── node ──► node1(val=3)
Step 3
B = HeapNode(node2)

Similarly:

B
 └── node ──► node2(val=5)
Step 4

When Python sees:

A < B

it automatically converts it to:

A.__lt__(B)

Now inside:

def __lt__(self, B):

Python assigns:

self = A
B    = B

So:

self.node.val < B.node.val

becomes:

A.node.val < B.node.val

Then:

node1.val < node2.val

Then:

3 < 5

which returns:

True
The key thing

When you write:

self.node = node

you are literally storing the passed node inside the object.

So after:

A = HeapNode(node1)

you can think of it as:

A.node = node1

and after:

B = HeapNode(node2)

you can think of it as:

B.node = node2

That's why inside __lt__ you can access:

A.node.val
B.node.val

and compare the actual ListNode values.'''