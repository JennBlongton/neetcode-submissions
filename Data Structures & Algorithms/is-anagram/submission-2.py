class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result_map = {}
        for c in s:
            if c not in result_map:
                result_map[c] = 1
            else:
                result_map[c]+= 1
        
        for c in t:
            if c in result_map:
                result_map[c] -= 1
            else:
                result_map[c] = 1

        for key, value in result_map.items():
            if value != 0:
                return False
        return True