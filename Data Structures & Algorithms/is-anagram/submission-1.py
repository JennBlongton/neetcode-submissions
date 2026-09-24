class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_data = {}
        for c in s:
            hash_data[c] = hash_data.get(c,0) + 1

        for c in t:
            if c not in hash_data:
                return False
            hash_data[c] -= 1
            if hash_data[c] < 0:
                return False
        return all(v == 0 for v in hash_data.values())