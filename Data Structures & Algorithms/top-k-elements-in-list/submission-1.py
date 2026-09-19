class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        
        pairs = []
        for key in res.keys():
            pairs.append((key, res[key]))
        print(pairs)

        final = [s[0] for s in sorted(pairs, key=lambda x: x[1],reverse=True)]
        return final[:k]
        