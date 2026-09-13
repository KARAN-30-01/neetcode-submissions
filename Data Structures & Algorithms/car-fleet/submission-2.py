class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = dict(zip(position, speed))
        position = sorted(position, reverse = True)
        timeStack = []
        for pos in position:
            time = (target - pos) / (car_dict[pos])
            if not timeStack or time > timeStack[-1]:
                timeStack.append(time)
        return len(timeStack)  



        