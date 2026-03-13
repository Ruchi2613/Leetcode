class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def insertNode(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insertNode(node.left, value)
        else:
            node.right = self.insertNode(node.right, value)
        return node

    def printTree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            self.printTree(node.left, level + 1, prefix="L--- ")
            self.printTree(node.right, level + 1, prefix="R--- ")

if __name__ == "__main__":
    tree = BinarySearchTree()
    values = [10, 5, 15, 12]
    root = None

    for val in values:
        root = tree.insertNode(root, val)

    tree.printTree(root)

'''BST (Binary Search Tree):
Values automatically sorted based on rules:

Left child < parent

Right child ≥ parent

'''


'''printTree(10)   → prints "Root: 10"
│
├── printTree(5) → prints "    L--- 5"
│   ├── None → return
│   └── None → return
│
└── printTree(15) → prints "    R--- 15"
    ├── printTree(12) → prints "        L--- 12"
    │   ├── None → return
    │   └── None → return
    └── None → return
'''