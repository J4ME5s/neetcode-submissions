class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in map:
                return [map[compl], i]
            map[nums[i]] = i