class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = []
        while 0 in nums:
            nums.remove(0)
            nums1.append(0)
        nums.extend(nums1)