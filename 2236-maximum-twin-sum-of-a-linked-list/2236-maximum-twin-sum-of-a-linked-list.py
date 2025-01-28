# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def pairSum(self, head: Optional[ListNode]) -> int:  
        if not head or not head.next:  
            return 0  

        length = 0  
        current_node = head  
        while current_node:  
            length += 1  
            current_node = current_node.next  

        mid = length // 2  
        current_node = head  
        
        stack = []  
        for _ in range(mid):  
            stack.append(current_node.val)  
            current_node = current_node.next  
            
        max_sum = float('-inf')  
        for _ in range(mid):  
            max_sum = max(max_sum, stack.pop() + current_node.val)  
            current_node = current_node.next  

        return max_sum 