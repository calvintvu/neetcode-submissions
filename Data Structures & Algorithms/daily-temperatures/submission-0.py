class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temp, index]
        res = [0 for _ in temperatures]

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            
            stack.append([t, i])
        
        return res
