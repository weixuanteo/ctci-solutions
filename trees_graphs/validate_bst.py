# Implement a function to check if a binary tree is a binary search tree.

from tree_node import TreeNode


def is_bst(root: TreeNode) -> bool:
    return dfs(root, float("-inf"), float("inf"))


def dfs(root: TreeNode, min: int, max: int) -> bool:
    if not root:
        return True
    if root.val <= min or root.val >= max:
        return False
    return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
