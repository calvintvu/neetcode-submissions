class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = {}

        for s in strs:

            sorted_str = "".join(sorted(s))

            if sorted_str not in cache.keys():
                cache[sorted_str] = [s]
            else:
                cache[sorted_str].append(s)
        
        res = []
        for i in cache.values():
            res.append(i)
        return res