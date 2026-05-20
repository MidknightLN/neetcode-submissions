class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key= lambda x:x[0],  reverse=True)
        # print(cars)
        ## 抵達終點所需要的時間 => Distance / speed
        stack = []
        count = 0
        for pos, spe in cars:
            curr_time = (target - pos) / spe

            if not stack or curr_time > stack[-1]:
                stack.append(curr_time)

        return len(stack)