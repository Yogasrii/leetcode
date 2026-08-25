class Solution:
    def canCompleteCircuit(self, gas, cost):
        # If total gas is less than total cost,
        # completing the circuit is impossible.
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # Current start cannot work
            if tank < 0:
                start = i + 1
                tank = 0

        return start