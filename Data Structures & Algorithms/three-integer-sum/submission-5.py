class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        length = len(nums) - 1
        res = []

        for i, n in enumerate(nums):
            
            # duplicate
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, length

            while l < r:
                
                if n + nums[l] + nums[r] > 0:
                    r -=1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res