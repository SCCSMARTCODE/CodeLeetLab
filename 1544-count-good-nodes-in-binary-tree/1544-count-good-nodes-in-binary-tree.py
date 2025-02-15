# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        root_node_count = 1
        left_count  = self.countGoodNodes(root.left, root.val)
        right_count = self.countGoodNodes(root.right, root.val)
        
        return root_node_count + left_count + right_count


    def countGoodNodes(self, node: TreeNode, max_value):
        if not node:
            return 0
        
        new_max_value = max(max_value, node.val)
        left_count = self.countGoodNodes(node.left, new_max_value)
        right_count = self.countGoodNodes(node.right, new_max_value)
        
        current_node_score = 0 if node.val < max_value else 1
        
        return left_count + right_count + current_node_score