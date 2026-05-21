class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 2 maps: TARGET, WINDOW
        target = Counter(t)
        targetCount = len(target)

        window = {}
        currCount = 0
        res = ""
        resLen = float("inf")
        
        l = 0
        for r in range(len(s)):
            currChar = s[r]
            window[currChar] = window.get(currChar, 0) + 1

            if currChar in target and window[currChar] == target[currChar]:
                currCount += 1
            
            while currCount == targetCount:
                # save to res first
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = len(res)

                # remove left pointer val from window
                leftChar = s[l]
                window[leftChar] -= 1

                # check if removed leftChar was a val in target
                if leftChar in target and window[leftChar] < target[leftChar]:
                    currCount -= 1
                l += 1
        return res