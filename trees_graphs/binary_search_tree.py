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
            return self._search_bst(value, self.root)
    
    def _search_bst(self, value, root) -> bool:
        if root is None:
            return False
        elif root.val == value:
            return True
        elif value < root.val:
            return self._search_bst(value, root.left)
        else:
            return self._search_bst(value, root.right)