# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return 0

        dq = deque()
        current_node = head

        while current_node is not None:
            dq.append(current_node.val)
            current_node = current_node.next

        max_sum = float('-inf')
        for _ in range(len(dq) // 2):
            max_sum = max(max_sum, dq.pop() + dq.popleft())

        return max_sum 