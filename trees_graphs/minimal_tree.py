# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#       5
#     /   \
#    2     8
#   / \   / \
#  1   3 6   9
#     /   \   \
#    4     7  10

from binary_search_tree import BinarySearchTree


def construct_minimal_tree(elements: list[int]) -> BinarySearchTree:
    tree = BinarySearchTree()
    if len(elements) == 0:
        return tree
    if len(elements) == 1:
        tree.add(elements[0])
        return tree
    add_elements_to_tree(tree, elements)
    return tree

def add_elements_to_tree(tree, elements):
    mid = len(elements) // 2
    tree.add(elements[mid])
    if mid > 0:
        add_elements_to_tree(tree, elements[:mid])
    if mid < len(elements) - 1:
        add_elements_to_tree(tree, elements[mid+1:])

def main():
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = construct_minimal_tree(elements)
    tree.print_tree()

if __name__ == '__main__':
    main()