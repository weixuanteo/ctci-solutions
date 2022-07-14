# T1 and T2 are very large binary trees, with T1 much bigger than T2. 
# Create an algorithm to determine if T2 is a subtree of T1

from tree_node import TreeNode

def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    if not t1:
        return False
    if is_same_tree(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def is_same_tree(t1: TreeNode, t2: TreeNode) -> bool:
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right) and t1.val == t2.val