class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sort = sorted(nums)
        mindiff = float('inf')
        for i, num in enumerate(sort):
            if i + k > len(sort):
                continue
            j = i + k - 1
            mindiff = min(sort[j] - sort[i], mindiff)
        return mindiff