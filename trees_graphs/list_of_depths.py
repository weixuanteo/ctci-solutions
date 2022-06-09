# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
# (e.g., if you have a tree with depth D, you'll have D linked lists).

from singly_linked_list import SinglyLinkedList
from tree_node import TreeNode

def create_level_linked_lists(root: TreeNode) -> list[SinglyLinkedList]:
    result = []
    current = SinglyLinkedList()
    if root:
        current.add_to_tail(root)

    while not current.is_empty():
        result.append(current.to_list())
        next_level = current
        current = SinglyLinkedList()
        while not next_level.is_empty():
            node = next_level.remove_from_head().data
            if node.left:
                current.add_to_tail(node.left)
            if node.right:
                current.add_to_tail(node.right)

    return result

def create_level_linked_lists_recursive(root: TreeNode, result: list[SinglyLinkedList], level: int) -> None:
    if not root:
        return
    if len(result) == level:
        result.append(SinglyLinkedList())
    result[level].add_to_tail(root)
    create_level_linked_lists_recursive(root.left, result, level + 1)
    create_level_linked_lists_recursive(root.right, result, level + 1)


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.right.right.right = TreeNode(8)

    result = create_level_linked_lists(tree)
    for r in result:
        print(r)

    result = []
    create_level_linked_lists_recursive(tree, result, 0)
    for r in result:
        print(r.to_list())

if __name__ == "__main__":
    main()
