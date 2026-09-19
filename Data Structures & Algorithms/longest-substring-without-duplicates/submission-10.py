class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        l = 0
        res = float('-inf')
        cache = set()
        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            res = max(res, r - l + 1)
        return res