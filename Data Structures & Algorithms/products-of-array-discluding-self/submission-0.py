class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        # l to r
        left = 1
        for i, n in enumerate(nums):
            res[i] = left
            left *= n
            print(res)
        
        # r to l
        right = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
            print(res)
            
        return (res)
