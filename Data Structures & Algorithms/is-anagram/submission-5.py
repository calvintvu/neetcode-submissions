class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        s_char_counts = Counter(s)
        t_char_counts = Counter(t)
        for key in s_char_counts.keys():
            if s_char_counts[key] != t_char_counts[key]:
                return False
        return True
