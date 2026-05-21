class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        reversedStr = cleaned_s[::-1]
        return cleaned_s == reversedStr