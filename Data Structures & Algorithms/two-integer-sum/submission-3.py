class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}

        for i, v in enumerate(nums):

            diff = target - v

            if diff in cache.keys():
                return [cache[diff], i]
            else:
                cache[v] = i
                
        return []