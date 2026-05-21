class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr = [0] * (2 * len(nums))
        for i in range(2):
            for j in range(len(nums)):
                newIndex = j
                if i == 1:
                    newIndex = j + len(nums)
                newArr[newIndex] = nums[j]
        return newArr