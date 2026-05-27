class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed
        sortedPos = []
        for x in range(len(position)):
            sortedPos.append([position[x], speed[x]])

        # Sort by position ascending so we can pop from the end (furthest first)
        sortedPos = sorted(sortedPos, key=lambda x: x[0])

        # Convert speed to time to reach target
        for x in sortedPos:
            x[1] = (target - x[0]) / x[1]

        fleets = 0
        lastTime = 0

        # Process from furthest to closest
        while sortedPos:
            time = sortedPos.pop()[1]
            if time > lastTime:
                fleets += 1
                lastTime = time  # this is the new fleet's arrival time
                # else: this car merges into the existing fleet

        return fleets
