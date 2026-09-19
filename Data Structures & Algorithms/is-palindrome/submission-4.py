class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = "".join(filter(str.isalnum, s)).lower()
        l, r = 0, len(clean_str) - 1

        while l < r:
            if clean_str[l] != clean_str[r]:
                return False
            l += 1
            r -= 1
        
        return True