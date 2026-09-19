class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in cache:
                return [cache[diff], idx]
            cache[n] = idx
        return []