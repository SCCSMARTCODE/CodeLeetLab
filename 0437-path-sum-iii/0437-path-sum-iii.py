class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.pathSumValue = 0
        prefix_sum = {0: 1} 
        self.dfs(root, 0, prefix_sum)
        return self.pathSumValue

    def dfs(self, node: Optional[TreeNode], current_sum: int, prefix_sum: Dict[int, int]):
        if not node:
            return

        current_sum += node.val

        self.pathSumValue += prefix_sum.get(current_sum - self.targetSum, 0)

        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        self.dfs(node.left, current_sum, prefix_sum)
        self.dfs(node.right, current_sum, prefix_sum)

        prefix_sum[current_sum] -= 1

        if prefix_sum[current_sum] == 0:
            del prefix_sum[current_sum]