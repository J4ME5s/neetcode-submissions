class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        maxLen = 0
        maxStr = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if self.isPalindrome(substr) and len(substr) > maxLen:
                    maxLen = len(substr)
                    maxStr = substr
        return maxStr
        
    def isPalindrome(self, s: str) -> int:
        rev = s[::-1]
        if rev == s:
            return 1
        return 0