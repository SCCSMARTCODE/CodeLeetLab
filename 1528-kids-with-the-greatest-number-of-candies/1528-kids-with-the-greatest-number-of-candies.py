class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for x in candies:
            result.append(x + extraCandies >= max(*candies))
        return result