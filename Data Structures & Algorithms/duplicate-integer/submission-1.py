class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        # nums_set = set(nums)
        # if len(nums_set) < len(nums):
        #     return True
        # return False

        # Approach 2
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False