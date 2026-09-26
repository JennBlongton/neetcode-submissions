class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) in [0, 1]:
            return [strs]
        
        seen = {}

        for i in range(len(strs)):
            sorted_key = "".join(sorted(strs[i]))
            if sorted_key not in seen:
                seen[sorted_key] = [strs[i]]
            else:
                seen[sorted_key].append(strs[i])


        return list(seen.values())