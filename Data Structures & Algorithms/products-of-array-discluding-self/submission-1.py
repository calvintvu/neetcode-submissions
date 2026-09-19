class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #      [1, 2, 3, 4]
        # pre  [1, 2, 6, 24]
        # post [24, 24, 12, 4]

        # res = [1 * 24, 1 * 12,  2 * 4, 6 * 1] = [24, 12, 8, 6]

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        print(prefix)
        
        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        print(suffix)
        
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res