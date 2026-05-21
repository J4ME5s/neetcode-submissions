class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for string in strs:
            newStr += str(len(string)) + "#" + string
        return newStr

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            j+=1
            strVal = s[j:j + length]
            result.append(strVal)
            i = j + length
        return result
