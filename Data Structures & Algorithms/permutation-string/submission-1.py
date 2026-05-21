class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1 = len(s1)
        length2 = len(s2)
        sortedS1 = "".join(sorted(s1))
        for i in range(length2 - length1 + 1):
            substr = s2[i:i+length1]
            sortedSub = "".join(sorted(substr))
            if sortedS1 == sortedSub:
                return True
        return False