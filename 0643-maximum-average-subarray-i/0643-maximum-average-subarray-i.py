from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_ = sum(nums[:k])
        i = k
        sec = max_
        while i < len(nums):
            sec = sec - nums[i - k] + nums[i]
            if sec > max_:
                max_ = sec
            i += 1
        return max_/k
