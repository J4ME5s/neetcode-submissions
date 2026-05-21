class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            char1 = s[i]
            char2 = s[i + 1]

            score += abs(ord(char2) - ord(char1))
        return score