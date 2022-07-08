# A binary search tree was created by traversing through an array from left and right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to it.
# EXAMPLE
# Input:
#     2
#    / \
#   1   3
# Output:
# [2, 1, 3], [2, 3, 1]

from tree_node import TreeNode


def all_sequences(root: TreeNode) -> list:
    if not root:
        return []
    return dfs(root)


def dfs(root: TreeNode) -> list:
    if not root:
        return [[]]
    left_seqs = dfs(root.left)
    right_seqs = dfs(root.right)
    seqs = []
    for left in left_seqs:
        for right in right_seqs:
            seqs = weave(left, right, [root.val], seqs)
    return seqs


def weave(list1: list, list2: list, prefix: list, result: list) -> list[list]:
    if not list1 and not list2:
        result.append(prefix)
    if list1:
        result = weave(list1[1:], list2, prefix + [list1[0]], result)
    if list2:
        result = weave(list1, list2[1:], prefix + [list2[0]], result)
    return result


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# print(all_sequences(root))
