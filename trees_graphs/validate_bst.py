# Implement a function to check if a binary tree is a binary search tree.

from tree_node import TreeNode

def is_bst(root: TreeNode) -> bool:
    if root is None:
        return True
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False
    return is_bst(root.left) and is_bst(root.right)