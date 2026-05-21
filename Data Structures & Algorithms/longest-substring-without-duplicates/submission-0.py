class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        seenChars = set()
        left = 0
        seenChars.add(s[left])
        maxLen = 1
        for right in range(1, len(s)):
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1
            seenChars.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen