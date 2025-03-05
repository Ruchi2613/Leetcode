'''1046. Last Stone Weight'''
import heapq
import math


def lastStoneWeight(stones):

    for x in range(len(stones)):
        stones[x] *= -1

    heapq.heapify(stones)
    print(stones)

    while len(stones) >1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)

        if stone1!=stone2:
            heapq.heappush(stones,stone1-stone2)

    if stones:
        return -heapq.heappop(stones)
    else:
        return 0
print(lastStoneWeight(stones=[2,2]))
# print(lastStoneWeight(stones=[2,7,4,1,8,1]))


'''2558. Take Gifts From the Richest Pile'''


def pickGifts(gifts, k):
    for x in range(len(gifts)):
        gifts[x] *= -1
    heapq.heapify(gifts)

    for j in range(k):
        largest = -heapq.heappop(gifts)
        rem_val = math.floor(largest ** (1 / 2)) * -1
        heapq.heappush(gifts, rem_val)

    return sum(gifts) * -1

print(pickGifts(gifts = [25,64,9,4,100], k = 4))

''''''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.idx = -1

    def build_tree(self, nodes):
        self.idx += 1
        if self.idx >= len(nodes) or nodes[self.idx] == -1:
            return None

        new_node = Node(nodes[self.idx])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        return new_node


if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.build_tree(nodes)
    print(root.data)

