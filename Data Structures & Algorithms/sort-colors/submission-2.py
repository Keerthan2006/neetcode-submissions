class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        n = len(nums)
        r = n - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[r],nums[i] = nums[i],nums[r]
                r -= 1
        return nums


        