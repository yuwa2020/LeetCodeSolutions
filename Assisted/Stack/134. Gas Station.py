class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_tank = 0
        current_tank = 0
        start_index = 0


        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            current_tank += diff
            total_tank += diff
            if current_tank <0:
                start_index = i+ 1
                current_tank = 0

        if total_tank >= 0:
            return start_index
        else:
            return -1