class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in buckets:
                buckets[sorted_s].append(s)
            else:
                buckets[sorted_s] = [s]
        return [value for value in buckets.values()]