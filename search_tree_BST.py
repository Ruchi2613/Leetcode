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


    def searchNode(self, node, key):
        if node is None:
            return False


        if key < node.value:# left subtree
            return self.searchNode(node.left, key)
        elif key > node.value: # right subtree
            return self.searchNode(node.right, key)
        elif key == node.value:
            return True
        else:
            return False


if __name__ == "__main__":
    tree = BinarySearchTree()
    values = [8,5,3,1,4,6,10,11,14]
    root = None

    for val in values:
        root = tree.insertNode(root, val)

    tree.printTree(root)

    if tree.searchNode(root, 12):
        print("Found")
    else:
        print("Not found")

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