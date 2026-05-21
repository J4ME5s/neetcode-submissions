class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[0] = 1
        maxLIS = 1
        for i in range(len(nums)):
            dp[i] = 1
            for k in range(0, i):
                if nums[i] > nums[k]:
                    if dp[k] + 1 > dp[i]:
                        dp[i] = dp[k] + 1
                        if dp[i] > maxLIS:
                            maxLIS = dp[i]
        return maxLIS