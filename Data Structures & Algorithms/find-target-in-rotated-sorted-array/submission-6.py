class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        originalEnd = end

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                # right side
                start = mid + 1
            else:
                # left side
                end = mid
        
        pivot = start
        start = 0
        if nums[pivot] <= target <= nums[originalEnd]:
            # right side
            start = pivot
            end = originalEnd
        else:
            # left side
            end = pivot - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # left side
                end = mid - 1
            else:
                # right side
                start = mid + 1
        
        return -1

