class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        length = len(nums)
        for i in range(length):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            cache[nums[i]] = i
