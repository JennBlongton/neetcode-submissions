class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (2 * len(nums))
        i = 0
        n = len(nums)

        while i < len(nums):
            result[i] = nums[i]
            result[i + n] = nums[i]
            i += 1

        return result