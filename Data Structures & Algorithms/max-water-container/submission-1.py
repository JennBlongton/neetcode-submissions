class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j-i)
        #         res = max(res, area)
        
        # return res

        # Optimized soln
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(area, res)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res