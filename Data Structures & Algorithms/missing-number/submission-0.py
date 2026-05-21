class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
        totalSum = 0
        for i in range(0, len(nums) + 1):
            totalSum = totalSum + i
        return totalSum - sum