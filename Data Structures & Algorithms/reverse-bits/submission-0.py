class Solution:
    def reverseBits(self, n: int) -> int:
        binStr = format(n, '032b')
        revBinStr = binStr[::-1]
        return int(revBinStr, 2)