class Solution:  
    def isSubsequence(self, s: str, t: str) -> bool:  
        cursor = 0  
        for chr_ in s:  
            cursor = t.find(chr_, cursor)  
            if cursor == -1:  
                return False  
            cursor += 1  
        return True 