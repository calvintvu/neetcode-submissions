class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        buckets = [[] for i in range(len(nums) + 1)]
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for number, count in counter.items():
            buckets[count].append(number)
        for b in reversed(buckets):
            if len(b) > 0:
                result.extend(b)
        return result[:k]