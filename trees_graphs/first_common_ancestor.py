# Design an algorithmn and write code to find the first common ancestor of two nodes in a binary tree. 
# Avoid storing additional nodes in a data structure.
# This is not necessarily a binary search tree.

from tree_node import TreeNode

def first_common_ancestor(first: TreeNode, second: TreeNode) -> TreeNode:
    depth1, depth2 = depth(first), depth(second)
    if depth1 > depth2:
        first, second = second, first

    for _ in range(abs(depth1 - depth2)):
        second = second.parent

    while first and second and first != second:
        first = first.parent
        second = second.parent

    return first if first and second else None

def depth(node: TreeNode) -> int:
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth
