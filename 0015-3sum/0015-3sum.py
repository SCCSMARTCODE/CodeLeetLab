class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            y, z = x + 1, len(nums) - 1
            
            while y < z:
                total = nums[x] + nums[y] + nums[z]
                
                if total == 0:
                    results.append([nums[x], nums[y], nums[z]])
                    
                    while y < z and nums[y] == nums[y + 1]:
                        y += 1
                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1
                    y += 1
                    z -= 1
                
                elif total < 0:
                    y += 1
                else:
                    z -= 1
        return results
        