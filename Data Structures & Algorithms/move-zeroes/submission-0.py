class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                r += 1
            else:
                nums[l],nums[r] = nums[r],nums[l]
                r += 1
                l += 1

        
        