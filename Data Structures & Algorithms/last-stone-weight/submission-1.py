class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # build a MAX heap
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        
        while len(pq) > 1:
            small1 = -1 * heapq.heappop(pq)
            small2 = -1 * heapq.heappop(pq)

            # destroy rules
            if small1 != small2:
                smaller = min(small1, small2)
                larger = small1 + small2 - smaller
                new = larger - smaller
                heapq.heappush(pq, -1 * new)
        
        return 0 if len(pq) == 0 else -1 * heapq.heappop(pq)
