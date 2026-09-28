class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [0] * n
        pref[0] =  1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        suff = [0] * n
        suff[n - 1] =  1
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        res = []
        for i in range(len(pref)):
            res.append(pref[i] * suff[i])
        return res
            

    
    # def productExceptSelfSlow(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i, n in enumerate(nums):
    #         product = 1
    #         for i_, n_ in enumerate(nums):
    #             if i == i_:
    #                 continue
    #             product *= n_
    #         res.append(product)
    #     return res