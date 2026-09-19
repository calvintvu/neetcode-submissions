class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # exclude = set("?", "!")
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        print(s)
        print(s[::-1])
        return s == s[::-1]