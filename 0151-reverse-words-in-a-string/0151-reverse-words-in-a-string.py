class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.strip().split()
        return ' '.join(reversed(output))