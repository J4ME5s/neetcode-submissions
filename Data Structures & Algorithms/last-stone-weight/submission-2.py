class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # build a MAX heap        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            small1 = -1 * heapq.heappop(stones)
            small2 = -1 * heapq.heappop(stones)

            # destroy rules
            if small1 > small2:
                new = small1 - small2
                heapq.heappush(stones, -1 * new)
        
        return 0 if len(stones) == 0 else -1 * heapq.heappop(stones)
