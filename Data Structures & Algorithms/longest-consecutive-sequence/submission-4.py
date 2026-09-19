class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        cache = set(nums)

        m = float('-inf')
        if not nums:
            return 0

        for n in cache:
            if (n - 1) not in cache:
                curr, temp = n, 0
                while n in cache:
                    temp += 1
                    n += 1
                m = max(m, temp)
        
        return m
