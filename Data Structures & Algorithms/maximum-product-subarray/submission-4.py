class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minDP = [0] * len(nums)
        maxDP = [0] * len(nums)

        minDP[0] = nums[0]
        maxDP[0] = nums[0]

        maxVal = nums[0]

        for i in range(1, len(nums)):
            minDP[i] = min(nums[i], maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i])
            maxDP[i] = max(nums[i], maxDP[i - 1] * nums[i], minDP[i - 1] * nums[i])
            maxVal = max(maxVal, minDP[i], maxDP[i])
        
        return maxVal