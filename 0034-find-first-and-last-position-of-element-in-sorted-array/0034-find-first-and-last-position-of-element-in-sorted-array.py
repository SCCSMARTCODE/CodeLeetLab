class Solution:  
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        def findLeftIndex(nums, target):  
            left, right = 0, len(nums) - 1  
            while left <= right:  
                mid = (left + right) // 2  
                if nums[mid] < target:  
                    left = mid + 1  
                else:  
                    right = mid - 1  
            return left  

        def findRightIndex(nums, target):  
            left, right = 0, len(nums) - 1  
            while left <= right:  
                mid = (left + right) // 2  
                if nums[mid] <= target:  
                    left = mid + 1  
                else:  
                    right = mid - 1  
            return right  
        
        left_index = findLeftIndex(nums, target)  
        right_index = findRightIndex(nums, target)  

        # Check if the target was found  
        if left_index <= right_index:  
            return [left_index, right_index]  
        else:  
            return [-1, -1] 