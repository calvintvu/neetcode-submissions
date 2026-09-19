class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = set()

        l = 0

        max_length = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            max_length = max(max_length, r - l + 1)
        
        return max_length

        # max_length = 0

        # if len(s) == 0:
        #     return 0

        # if len(s) == 1:
        #     return 1

        # l, r = 0, 1

        # substring = set()

        # while r < len(s):

        #     substring.add(s[l])
        #     max_length = max(max_length, len(substring))
        #     print(substring)

        #     if s[r] not in substring:
        #         substring.add(s[r])
        #         print(substring)
        #         max_length = max(max_length, len(substring))
        #         r += 1

        #     else:
        #         substring.clear()
        #         l = r
        #         r += 1

        # return max_length