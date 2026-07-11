class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            length = 0
            if num - 1 in numSet:
                continue
            i = 0
            while num + i in numSet:
                length += 1
                i += 1
            longest = max(longest,length)
        return longest



        