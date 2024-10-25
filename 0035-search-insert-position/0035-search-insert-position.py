class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            center = (left + right) // 2

            if nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center + 1
            else:
                return center
        return left