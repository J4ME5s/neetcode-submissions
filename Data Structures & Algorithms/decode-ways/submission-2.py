class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[0] = 0 if s[0] == '0' else 1
        if len(s) == 1:
            return dp[0]
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            # consider s[i]
            oneDigit = 0
            if s[i-1] != '0':
                oneDigit += dp[i - 1]

            # consider s[i - 1: i + 1]
            twoDigit = 0
            if s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
                twoDigit += dp[i - 2]
            
            dp[i] = oneDigit + twoDigit
        return dp[len(s)]
