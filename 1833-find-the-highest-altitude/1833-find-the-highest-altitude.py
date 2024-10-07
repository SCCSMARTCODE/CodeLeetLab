class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        alt_sum = 0
        for height in gain:
            alt_sum += height
            if alt_sum > highest_altitude:
                highest_altitude = alt_sum
        return highest_altitude