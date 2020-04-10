class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1


"""
算法来说不难， 这题是存在唯一一个点，使得能走完全程
这题有一个规律是，假如说再当前节点  gas[i] - cost[i] < 0
是不可能完成任务的
所以我们假如说要完成任务，我们需要准备两个条件
1. total tank走完全程是正数
2. cur_tank小于0的时候，说明当前节点不行，要换到下一个节0点
"""