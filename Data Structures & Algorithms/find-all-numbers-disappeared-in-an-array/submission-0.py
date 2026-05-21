class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        sortedNums = sorted(nums)
        n = len(nums)
        for i in range(1, len(nums) + 1):
            if (i not in sortedNums):
                res.append(i)
        return res