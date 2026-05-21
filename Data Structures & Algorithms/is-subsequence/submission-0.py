class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        build = ""
        while i < len(s) and j < len(t):
            curr = s[i]
            if t[j] == curr:
                build += t[j]
                i += 1
                j += 1
            else:
                j += 1
        return build == s