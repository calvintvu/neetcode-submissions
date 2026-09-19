class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:

            cur_area = (r - l) * min(heights[r], heights[l])

            max_area = max(max_area, cur_area)

            if heights[l] <= heights[r]:
                l += 1

            elif heights[l] > heights[r]:
                r -= 1
        
        return max_area

