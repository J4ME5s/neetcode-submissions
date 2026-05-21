class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        count = 0
        for i in range(l, r + 1):
            if blocks[i] == 'W':
                count += 1

        best = count

        while r < len(blocks) - 1:
            if blocks[l] == 'W':
                count -= 1
            l += 1
            r += 1
            if blocks[r] == 'W':
                count += 1
            best = min(best, count)
        return best
