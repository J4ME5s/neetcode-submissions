class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        i = 0
        for pt in points:
            x, y = pt
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(pq, (dist, i))
            i += 1
        
        res = []
        while k > 0:
            dist, i = heapq.heappop(pq)
            res.append(points[i])
            k -= 1
        
        return res
        
        