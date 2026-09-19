class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter

        freq = Counter(nums)

        buckets = [[] for _ in nums]

        for key in freq.keys():
            buckets[freq[key] - 1].append(key)
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) == k:
                break
        
        return res