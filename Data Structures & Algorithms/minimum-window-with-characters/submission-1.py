class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = Counter(t)
        reqCount = len(targetMap)

        window = {}
        currCount = 0
        l = 0
        res = ""
        resLen = float("inf")
        for r in range(len(s)):
            currChar = s[r]
            window[currChar] = window.get(currChar, 0) + 1

            if currChar in targetMap and window[currChar] == targetMap[currChar]:
                currCount += 1
            
            # try shrinking window
            while reqCount == currCount:
                # update possible res
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                leftChar = s[l]
                window[leftChar] -= 1
                if leftChar in targetMap and window[leftChar] < targetMap[leftChar]:
                    currCount -= 1
                l +=1
        return res
        