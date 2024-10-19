class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        nums_med = len(nums1)/2
        if nums_med % 1 != 0:
            return nums1[int(nums_med)]
        else:
            return (nums1[int(nums_med)-1] + nums1[int(nums_med)]) / 2