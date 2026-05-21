class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(0, n + 1):
            binStr = format(i, '032b')
            counter = 0
            for j in range(0, len(binStr)):
                subStr = binStr[j:j+1]
                if subStr == '1':
                    counter = counter + 1
            result[i] = counter
        return result
