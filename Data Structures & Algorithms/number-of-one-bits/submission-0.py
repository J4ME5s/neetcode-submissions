class Solution:
    def hammingWeight(self, n: int) -> int:
        # drop the 0b prefix
        binStr = format(n, '032b')
        counter = 0
        for i in range(0, len(binStr)):
            subStr = binStr[i:i+1]
            if subStr == '1':
                counter = counter + 1
        return counter