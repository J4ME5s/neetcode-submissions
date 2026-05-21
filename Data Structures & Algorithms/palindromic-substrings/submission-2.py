class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        count = 0

        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if i == j:
                    dp[i][j] = 1
                    count += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    count += 1
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    count += 1

        return count
        