from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = Counter(nums)
        
        for num in nums:
            complement = k - num
            if num_count[num] > 0 and num_count[complement] > 0:
                if num == complement:
                    pairs = num_count[num] // 2
                    count += pairs
                    num_count[num] -= pairs * 2
                else:
                    pairs = min(num_count[num], num_count[complement])
                    count += pairs
                    num_count[num] -= pairs
                    num_count[complement] -= pairs
        
        return count