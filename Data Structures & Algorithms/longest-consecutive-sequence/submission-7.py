class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        from_list = set(nums)
        longest = 1
        for n in nums:
            # start sequence
            if n - 1 not in from_list:
                start = n
                curr_len = 1
                while start + 1 in from_list:
                    curr_len += 1
                    start += 1
                    longest = max(longest, curr_len)
        return longest