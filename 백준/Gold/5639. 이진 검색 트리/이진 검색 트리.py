import sys

sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insertNode(self.root, val)

    def _insertNode(self, currentNode: Node, val):
        # if val <= currentNode.val:
        #     if currentNode.leftChildChild:
        #         self._insertNode(currentNode.leftChildChild, val)
        #     else:
        #         currentNode.leftChildChild = Node(val)
        # else:
        #     if currentNode.rightChild:
        #         self._insertNode(currentNode.rightChild, val)
        #     else:
        #         currentNode.rightChild = Node(val)
        while True:
            if val < currentNode.val:
                if currentNode.leftChild == None:
                    currentNode.leftChild = Node(val=val)
                    break
                else:
                    currentNode = currentNode.leftChild
            else:
                if currentNode.rightChild == None:
                    currentNode.rightChild = Node(val=val)
                    break
                else:
                    currentNode = currentNode.rightChild

    def postorder_traversal(self, node: Node):
        if node.leftChild:
            self.postorder_traversal(node.leftChild)
        if node.rightChild:
            self.postorder_traversal(node.rightChild)
        print(node.val)


# if val <= currentNode.val:
#             if currentNode.leftChildChild:
#                 self._insertNode(currentNode.leftChildChild, val)
#             else:
#                 currentNode.leftChildChild = Node(val)
#         else:
#             if currentNode.rightChild:
#                 self._insertNode(currentNode.rightChild, val)
#             else:
#                 currentNode.rightChild = Node(val)


a = []
while True:
    try:
        a.append(int(input()))
    except EOFError:
        break

tree = BinarySearchTree()

for i in range(len(a)):
    tree.insert(a[i])

tree.postorder_traversal(tree.root)
