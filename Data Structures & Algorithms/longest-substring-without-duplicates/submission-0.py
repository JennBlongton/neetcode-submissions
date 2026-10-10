class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        tempset = set()

        while right < len(s):
            while s[right] in tempset:
                tempset.remove(s[left])
                left += 1
            tempset.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        
        return res
