class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        # Base Case: diagonal is all valid palindromes
        count = 0
        for r in range(len(s)):
            for c in range(r, len(s)):
                if r == c:
                    dp[r][c] = 1
                    count += 1
                else:
                    substr = s[r:c+1]
                    revSubstr = substr[::-1]
                    if substr == revSubstr:
                        dp[r][c] = 1
                        count += 1
                    else:
                        dp[r][c] = 0
        return count