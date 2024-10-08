class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        chrs = ""

        list_len = min([len(str_) for str_ in strs])

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