class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        solution = [list(nums1.difference(nums2)), list(nums2.difference(nums1))]
        return solution