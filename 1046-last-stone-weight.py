

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones = sorted(stones, reverse=True)
            value = stones[0] - stones[1]
            # print(stones[0], '-', stones[1], '=', value)
            if value > 0:
                stones = stones[2:]
                stones.append(value)
            else:
                stones = stones[2:]
        try:
            return stones[0]
        except:
            return 0