class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            height = min(heights[l],heights[r])
            width = r - l
            area = height * width
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_water = max(max_water,area)
        return max_water