class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        
        best = count

        l = 0
        r = k - 1
        while r < len(blocks) - 1:
            if blocks[l] == 'W':
                count -= 1
            l += 1
            r += 1
            if blocks[r] == 'W':
                count += 1
            best = min(best, count)
        return best