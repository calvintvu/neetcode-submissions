class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:

            m = (l + r) // 2

            # check how long eating piles will take
            time = 0
            for p in piles:
                time += math.ceil(float(p) / m)
            
            if time <= h:
                # go left
                res = m
                r = m - 1
            
            else:
                # go right
                l = m + 1
        
        return res