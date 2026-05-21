class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Case
        if len(nums) == 1:
            return nums[0]

        # DP Recursion
        excludeLast = self.robLinear(nums[0:len(nums)-1])
        excludeFirst = self.robLinear(nums[1:len(nums)])
        return max(excludeLast, excludeFirst)
        
    def robLinear(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        
        return dp[len(nums)]