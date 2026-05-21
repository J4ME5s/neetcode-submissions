class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, curr):
            res.append(list(curr))
            for i in range(start, len(nums)):
                # skip dupes
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # include current number
                curr.append(nums[i])
                backtrack(i + 1, curr)
                # exclude current number
                curr.pop()

        res = []
        nums.sort()
        backtrack(0, [])
        return res

