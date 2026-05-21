class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
            else:
                return True
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False