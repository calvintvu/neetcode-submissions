class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        no_whitespace = "".join(lower.split())
        cleaned_text = "".join(c for c in no_whitespace if c.isalnum())
        l, r = 0, len(cleaned_text) - 1
        while l < r:
            if cleaned_text[l] != cleaned_text[r]:
                return False
            l += 1
            r -= 1
        return True
        