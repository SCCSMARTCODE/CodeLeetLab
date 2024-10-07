class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        equal_pairs = 0

        for x in grid:
            for y in zip(*grid):
                if x == list(y):
                    equal_pairs += 1
        return equal_pairs