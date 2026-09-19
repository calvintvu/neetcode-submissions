class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in cache:
                cache[sorted_str] = [s]
            else:
                cache[sorted_str] += [s]
        res = []
        for lst in cache.values():
            res += [lst]
        return res
        