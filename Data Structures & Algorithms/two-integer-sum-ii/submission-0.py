class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total_sum = numbers[l] + numbers[r]
            if total_sum == target:
                return [l+1,r+1]
            elif total_sum > target:
                r -= 1
            else:
                l += 1
        