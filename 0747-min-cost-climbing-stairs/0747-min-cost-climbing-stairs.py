from typing import List  

class Solution:  
    def minCostClimbingStairs(self, cost: List[int]) -> int:  
        n = len(cost)  
        
        dp = [0] * (n + 1)  
        
        dp[0] = 0
        dp[1] = 0   

        for i in range(2, n + 1):  
            dp[i] = min(dp[i - 1] + (cost[i - 1] if i - 1 < n else 0),  
                         dp[i - 2] + (cost[i - 2] if i - 2 < n else 0))  
        
        return dp[n]  
