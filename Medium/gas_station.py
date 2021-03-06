"""
There are N gas stations along a circular route,
where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it
costs cost[i] of gas to travel from station i to
its next station (i+1). You begin the journey with
an empty tank at one of the gas stations.
Return the starting gas station's index if you can
travel around the circuit once in the clockwise
direction, otherwise return -1.
Note:
If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n, start, surplus, diff = len(gas), 0, 0, 0
        for i in range(n):
            diff += (gas[i] - cost[i])
            surplus += (gas[i] - cost[i])
            if surplus < 0:
                surplus = 0
                start = (i + 1) % n
        return start if diff >= 0 else -1

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
    if ex_0 != 3:
        print("Error")
    # Explanation:
    # Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    # Travel to station 4. Your tank = 4 - 1 + 5 = 8
    # Travel to station 0. Your tank = 8 - 2 + 1 = 7
    # Travel to station 1. Your tank = 7 - 3 + 2 = 6
    # Travel to station 2. Your tank = 6 - 4 + 3 = 5
    # Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    # Therefore, return 3 as the starting index.
    ex_0 = s.canCompleteCircuit([2,3,4], [3,4,3])
    if ex_0 != -1:
        print("Error")
    # Explanation:
    # You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    # Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    # Travel to station 0. Your tank = 4 - 3 + 2 = 3
    # Travel to station 1. Your tank = 3 - 3 + 3 = 3
    # You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    # Therefore, you can't travel around the circuit once no matter where you start.
    ex_0 = s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])
    if ex_0 != 4:
        print("Error")
    ex_0 = s.canCompleteCircuit([3,1,1], [1,2,2])
    if ex_0 != 0:
        print("Error")
    pass