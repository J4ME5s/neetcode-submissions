class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def backtrack(path, nums, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path, nums, used)
                    path.pop()
                    used[i] = False
        
        res = []
        backtrack([], nums, [False] * len(nums))
        return res
