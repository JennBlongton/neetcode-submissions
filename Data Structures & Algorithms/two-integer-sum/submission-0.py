class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        l = len(nums)

        for i in range(l - 1):
            for j in range(l):
                if i != j:
                    if nums[i] + nums[j] == target:
                        res = [i, j]

        return sorted(res)