class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0 
        count = {}
        
        # left ptr is for shrinking window
        l = 0
        # right ptr is for expanding window
        for r in range(len(s)):

            # update count of letters in window
            count[s[r]] = 1 + count.get(s[r], 0)

            # if len(window) - max(values), then window is valid
            # else, shrink the window, and update count
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res