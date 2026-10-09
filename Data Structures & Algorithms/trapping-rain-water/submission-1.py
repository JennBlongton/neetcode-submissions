class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute force
        n = len(height)
        if n == 0:
            return 0
        # res = 0

        # for i in range(1, len(height)-1):
        #     left_max = max(height[:i])
        #     right_max = max(height[i:])
        #     water = max(0, min(left_max, right_max) - height[i])
        #     res += water

        # return res

        # Optimized soln
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
