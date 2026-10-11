class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        left = 0
        window_size = len(s1)

        for right in range(len(s2)):
            ch = s2[right]
            count2[ch] = count2.get(ch, 0) + 1

            if right - left + 1 > window_size:
                left_char = s2[left]
                count2[left_char] -= 1

                if count2[left_char] == 0:
                    del count2[left_char]

                left += 1
            # Check whether the window is a permutation of s1
            if right - left + 1 == window_size and count1 == count2:
                return True


        return False