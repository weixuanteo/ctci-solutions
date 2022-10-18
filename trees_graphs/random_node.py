# You are implementing a binary tree from scratch which, in addition to insert, find, and delete,
# has a method getRandomNode() which returns a random node from the tree.
# All nodes should be equally likely to be chosen.
# Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.

from tree_node import TreeNode
from collections import deque
import random


def get_random_node(root: TreeNode) -> TreeNode:
    nodes = []
    if not root:
        return None

    # BFS level traversal
    q = deque([root])
    while q:
        q_len = len(q)
        for i in range(q_len):
            node = q.popleft()
            nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return nodes[random.randint(0, len(nodes) - 1)]


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
seven = TreeNode(7)
eight = TreeNode(8)

one.left = two
one.right = three
three.left = seven
three.right = eight

print(get_random_node(one))
