from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numPiles = len(piles)
        numBananas = 0
        for i in range(len(piles)):
            numBananas += piles[i]
        
        # compute candidate k val
        start = 1
        end = max(piles)
        while start < end:
            mid = (start + end) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)
            
            if hours <= h:
                end = mid
            else:
                start = mid + 1
        return start