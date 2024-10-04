class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        chrs = ""
        list_len = len(strs[0])
        for str_ in strs:
            str_len = len(str_)
            if list_len > str_len:
                list_len = str_len

        while i < list_len:
            pre_chr = strs[0][i]
            j = 0
            while j < len(strs):
                if strs[j][i] != pre_chr:
                    return chrs
                j += 1
            chrs += pre_chr
            i += 1
        return chrs