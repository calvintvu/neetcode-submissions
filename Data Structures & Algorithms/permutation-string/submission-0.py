class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False
        
        l = 0
        count_s2, count_s1 = {}, {}

        for s in s1:
            count_s1[s] = 1 + count_s1.get(s, 0)

        for r in range(len_s2):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)
            
            print(count_s2, count_s1)
            # fixed window
            if (r - l + 1) == len_s1:
                
                # print(count_s2, count_s1)
                if count_s2 == count_s1:
                    return True

                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    count_s2.pop(s2[l])
                l += 1
        
        return False


