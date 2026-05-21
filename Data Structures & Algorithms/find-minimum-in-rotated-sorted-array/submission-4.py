class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[left]:
            return nums[0]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                if right - left == 1:
                    return nums[right]
                # right side
                left = mid + 1
            elif nums[mid] < nums[right]:
                if right - left == 1:
                    return nums[left]
                # left side
                right = mid
        return nums[left]