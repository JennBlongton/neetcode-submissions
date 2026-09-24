class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
                return True

        return False
