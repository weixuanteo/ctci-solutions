# Implemenation of Binary Tree Travesals

from tree_node import TreeNode

def visit(node: TreeNode, result: list):
    result.append(node.val)

def preorder(root: TreeNode, result: list) -> list:
    if root is None:
        return
    visit(root, result)
    preorder(root.left, result)
    preorder(root.right, result)
    return result

def inorder(root: TreeNode, result: list) -> list:
    if root is None:
        return
    inorder(root.left, result)
    visit(root, result)
    inorder(root.right, result)
    return result

def postorder(root: TreeNode, result: list) -> list:
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    visit(root, result)
    return result