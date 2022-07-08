from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_to_bst(value, self.root)

    def _add_to_bst(self, value, root):
        if value < root.val:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self._add_to_bst(value, root.left)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self._add_to_bst(value, root.right)

    def contains(self, value) -> bool:
        if self.root is None:
            return False
        else:
            result = self._search_bst(value, self.root)
            if result is None:
                return None
            return value == result.val

    def search(self, value) -> TreeNode:
        if self.root is None:
            return None
        else:
            return self._search_bst(value, self.root)

    def _search_bst(self, value, root) -> bool:
        if root is None:
            return None
        elif root.val == value:
            return root
        elif value < root.val:
            return self._search_bst(value, root.left)
        else:
            return self._search_bst(value, root.right)

    def print_tree(self):
        # print binary tree by levels
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()

    def get_structure_by_levels(self) -> list:
        # print binary tree by levels
        if self.root is None:
            return []
        queue = [self.root]
        result = []
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result
