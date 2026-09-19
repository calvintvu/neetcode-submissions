class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_spd = list(zip(position, speed))
        pos_spd.sort(key=lambda x: x[0], reverse=True)

        print(pos_spd)

        stack = []

        for car in pos_spd:

            cur_car_time = (target - car[0]) / car[1]

            if stack:
                # If the current car's time is less than or equal to the top of the stack, it joins the same fleet
                stack_car_time = (target - stack[-1][0]) / stack[-1][1]
                if cur_car_time <= stack_car_time:
                    # stack[-1].append(car)
                    continue

            stack.append(car)
        
        print(stack)
        return len(stack)