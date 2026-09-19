class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cache = {}
        # for n in nums:
        #     if n - 1 not in cache:
        #         cache[n] = [n]
        #     elif n - 1 in cache:
        #         cache[n] = cache[n - 1] + [n]
        #     elif n + 1 in cache:
        #         cache[n] = cache[n + 1] + [n]
        # print(cache)
        # max_key = max(cache, key= lambda x: len(set(cache[x])))
        # return len(cache[max_key])
        cache = set(nums)
        longest = 0
        for n in cache:
            if (n - 1) not in cache:
                # no left neighbor -> start of sequence
                length = 0
                while (n + length) in cache:
                    length += 1
                longest = max(length, longest)
        return longest
