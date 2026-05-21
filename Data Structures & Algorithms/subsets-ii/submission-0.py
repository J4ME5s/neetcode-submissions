class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, curr):
            res.append(list(curr))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # include
                curr.append(nums[i])
                backtrack(i + 1, curr)
                # exclude
                curr.pop()
        
        res = []
        nums.sort()
        backtrack(0, [])
        return res