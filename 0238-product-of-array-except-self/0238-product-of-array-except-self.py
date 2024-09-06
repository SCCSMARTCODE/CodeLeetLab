class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        str_ = "*".join([str(num) for num in nums])
        total = eval(str_)
        answer = [int(total/val) if val != 0 else eval(str_.replace('*0' if '*0' in str_ else '0*', '', 1)) for val in nums]
        return answer
        