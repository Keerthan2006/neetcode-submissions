class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # left = [1,1,2,8]
    # right = [48,24,6,1] => [48,24,12,8]
        l_mult = 1
        r_mult = 1
        n = len(nums)
        prefix_list = [0] * n
        suffix_list = [0] * n
        
        for i in range(n):
            j = n - i - 1
            prefix_list[i] = l_mult
            suffix_list[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        res = []
        for i in range(n):
            res.append(prefix_list[i]*suffix_list[i])
        return res

            
        