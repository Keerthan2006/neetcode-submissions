class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        smallest = float("inf")
        n = len(nums)
        current_sum = 0
        current_len = 0
        for r in range(n):
            current_sum += nums[r]
            while current_sum >= target:
                current_len = r - l + 1
                current_sum -= nums[l]
                l += 1
                smallest = min(smallest,current_len)
        return 0 if smallest == float("inf") else smallest



        