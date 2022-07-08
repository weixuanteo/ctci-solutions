# Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

from tree_node import TreeNode


def find_successor(node: TreeNode) -> TreeNode:
    if node.right:
        return find_min(node.right)
    else:
        while is_right_child(node):
            node = node.parent
        return node.parent


def find_min(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node


def is_right_child(node: TreeNode) -> bool:
    return node.parent and node.parent.right == node


def main():
    # Create a binary search tree with the following values with parent: 4, 2, 1, 3, 6, 5, 7, 10, 9, 8
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.parent = root
    root.left.left = TreeNode(1)
    root.left.left.parent = root.left
    root.left.right = TreeNode(3)
    root.left.right.parent = root.left
    root.right = TreeNode(6)
    root.right.parent = root
    root.right.left = TreeNode(5)
    root.right.left.parent = root.right
    root.right.right = TreeNode(7)
    root.right.right.parent = root.right
    root.right.right.right = TreeNode(10)
    root.right.right.right.parent = root.right.right
    root.right.right.right.left = TreeNode(9)
    root.right.right.right.left.parent = root.right.right.right
    root.right.right.right.left.left = TreeNode(8)
    root.right.right.right.left.left.parent = root.right.right.right.left

    # Find the successor of the node with value 6
    successor = find_successor(root.right)
    print(successor)

    # Find the successor of the node with value 10
    successor = find_successor(root.right.right.right)
    print(successor)


if __name__ == "__main__":
    main()
