class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        # create hashmap to count freq of elements
        counter = Counter(nums)
        print(counter)

        # create empty list with size of nums
        # max freq is size of nums
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)

        # populate each bucket
        for element, freq in counter.items():
            buckets[freq].append(element)
        print(buckets)

        res = []
        top_k = k

        for i in range(len(buckets) - 1, -1, -1):
            if top_k == 0:
                break
            if buckets[i]:
                for elem in buckets[i]:
                    res.append(elem)
                    top_k -= 1
                    if top_k == 0:
                        break
        
        print(res)
        return res
            