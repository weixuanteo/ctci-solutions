# Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more than one.

from tree_node import TreeNode


def is_balanced(root: TreeNode) -> bool:
    if root is None:
        return True
    return (
        abs(height(root.left) - height(root.right)) < 2
        and is_balanced(root.left)
        and is_balanced(root.right)
    )


def height(root: TreeNode):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
