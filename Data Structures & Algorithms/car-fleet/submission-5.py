import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 3, 5, 10, 3
        # 1, 1, 12, 7, 3
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []

        for x in range(len(cars)):

            curr = (target - cars[x][0]) / cars[x][1]

            if fleets and curr <= fleets[-1]:

                continue

            else:

                fleets.append(curr)

        return len(fleets)