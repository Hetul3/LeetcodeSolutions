# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        val_to_depth = {}
        def dfs_with_depth(root, level):
            if not root:
                return
            val_to_depth[root] = level
            dfs_with_depth(root.left, level+1)
            dfs_with_depth(root.right, level+1)
        dfs_with_depth(root, 0)
        deepest_depth, deepest_nodes = 0, set()
        for key, val in val_to_depth.items():
            if val > deepest_depth:
                deepest_depth = val
                deepest_nodes = set()
            if val == deepest_depth:
                deepest_nodes.add(key)
        result_node = None
        def dfs(root):
            nonlocal result_node
            if result_node:
                return set()
            if not root:
                return set()
            set1 = dfs(root.left)
            set2 = dfs(root.right)
            larger_set = set1.union(set2)
            if result_node:
                return set()
            larger_set.add(root)
            if deepest_nodes.issubset(larger_set):
                result_node = root
                return set()
            return larger_set
        dfs(root)
        return result_node