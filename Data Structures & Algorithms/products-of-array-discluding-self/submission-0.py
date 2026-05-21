class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)

        j = len(nums) - 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i == 1:
                prefix[i] = nums[i - 1]
            elif i > 1:
                prefix[i] = nums[i - 1] * prefix[i - 1]
            
            if j == len(nums) - 2:
                suffix[j] = nums[j + 1]
            elif j < len(nums) - 2:
                suffix[j] = nums[j + 1] * suffix[j + 1]
        
        final = [None] * len(nums)
        final[0] = suffix[0]
        for i in range(1, len(nums) - 1):
            final[i] = prefix[i] * suffix[i]
        final[len(nums) - 1] = prefix[len(nums) - 1]
        return final