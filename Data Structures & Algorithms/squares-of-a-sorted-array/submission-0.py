class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nonNegIndex = 0
        for n in nums:
            if n < 0:
                nonNegIndex += 1
        l, r = nonNegIndex - 1, nonNegIndex
        res = []
        while l >= 0 and r < len(nums):
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[l]**2)
                l -= 1
            else:
                res.append(nums[r]**2)
                r += 1
        while l >= 0:
            res.append(nums[l]**2)
            l -= 1
        while r < len(nums):
            res.append(nums[r]**2)
            r += 1
        return res