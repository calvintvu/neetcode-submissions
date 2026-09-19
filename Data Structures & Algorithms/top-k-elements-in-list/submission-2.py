class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for key in counter.keys():
            freq[counter[key]] += [key]
        
        res = []
        for i in range (len(nums), 0, -1):
            if freq[i]:
                res += freq[i]
            if len(res) == k:
                break
        return res