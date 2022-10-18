# Given a binary tree where each node contains negative or positive values
# Design an algorithm to count the number of paths that sum to a given value
# Path does not need to start from root and end at leaf, but it must go downwards

from tree_node import TreeNode


def count_paths(root: TreeNode, target: int) -> int:
    sum_to_path_count = {}

    def dfs(node, target_sum, running_sum):
        if not node:
            return 0
        running_sum += node.val
        sum = running_sum - target_sum
        total_paths = sum_to_path_count.get(sum, 0)

        if running_sum == target_sum:
            total_paths += 1

        sum_to_path_count[running_sum] = sum_to_path_count.get(running_sum, 0) + 1
        total_paths += dfs(node.left, target_sum, running_sum)
        total_paths += dfs(node.right, target_sum, running_sum)
        sum_to_path_count[running_sum] -= 1
        return total_paths

    return dfs(root, target, 0)


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(-3)
d = TreeNode(3)
e = TreeNode(1)
f = TreeNode(11)
g = TreeNode(3)
h = TreeNode(-2)
i = TreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
d.right = h
e.right = i

print(count_paths(a, 8))
