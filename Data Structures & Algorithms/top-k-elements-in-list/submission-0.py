class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        sorted_seen = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        for item in sorted_seen:
            if len(result) == k:
                break

            result.append(item[0])
        
        return result
