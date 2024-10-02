from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s_array = [1 if c in vowels else 0 for c in s]

        max_ = sum(s_array[:k])
        i = k
        sec = max_
        while i < len(s_array):
            sec = sec - s_array[i - k] + s_array[i]
            if sec > max_:
                max_ = sec
            i += 1
        return max_
