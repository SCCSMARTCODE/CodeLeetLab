class Solution:
    def removeStars(self, s: str) -> str:
        out_s = ""
        star_count = 0
        i = len(s)-1

        while i >= 0:
            if s[i] == '*':
                star_count += 1
            elif star_count:
                star_count -= 1
            else:
                out_s = s[i] + out_s
            i -= 1
        return out_s