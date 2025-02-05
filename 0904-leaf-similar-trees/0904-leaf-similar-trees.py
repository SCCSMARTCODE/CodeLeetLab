# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:  
        first_list = []  
        second_list = []  
        
        self.dig(root1, first_list)  
        self.dig(root2, second_list)  
        
        return first_list == second_list  
        
    def dig(self, node: Optional[TreeNode], _list: List[int]):  
        if node is None:  
            return  
        if not node.left and not node.right:  
            _list.append(node.val)  
        else:  
            self.dig(node.left, _list)  
            self.dig(node.right, _list) 
