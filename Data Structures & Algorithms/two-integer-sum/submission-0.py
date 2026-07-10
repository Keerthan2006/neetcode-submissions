class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in checker:
                return [checker[target_value],i]
            checker[nums[i]] = i


        