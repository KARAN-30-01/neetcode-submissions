class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = {}

        for i in range(len(position)):
            cars[position[i]] = speed[i]

        # Closest to target first
        cars = dict(sorted(cars.items(), reverse=True))

        times = []
        fleets = 0

        for pos, spd in cars.items():
            time = (target - pos) / spd

            if not times or time > times[-1]:
                fleets += 1
                times.append(time)

        return fleets