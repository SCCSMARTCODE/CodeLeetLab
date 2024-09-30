class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height) - 1
        rev_height = list(reversed(height))
        max_area = 0
        i = j = 0
        h_length = len(height)

        while i < h_length and j < h_length and width:
            h, is_height = min(height[i], rev_height[j]), height[i] < rev_height[j]
            area = width * h
            if area > max_area:
                max_area = area
            if is_height:
                i += 1
                width -= 1
            else:
                j += 1
                width -= 1
        return max_area