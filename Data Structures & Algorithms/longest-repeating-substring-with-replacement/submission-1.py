class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute sln
        # res = 0

        # for left in range(len(s)):
        #     count = {}
        #     max_freq = 0
        #     for right in range(left, len(s)):
        #         ch = s[right]
        #         count[ch] = count.get(ch, 0) + 1
        #         max_freq = max(max_freq, count[ch])

        #         window_length = right - left + 1
        #         replacement = window_length - max_freq

        #         if replacement <= k:
        #             res = max(res, window_length)
        
        # return res

        # Optimized solution
        res = 0
        left = 0
        counts = {}

        for right in range(len(s)):
            ch = s[right]
            counts[ch] = counts.get(ch, 0) + 1
            
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
