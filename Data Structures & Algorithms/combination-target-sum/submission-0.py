class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(index, sum, path):
            if sum == target:
                result.append(path)
                return
            if index == len(nums) or sum > target:
                return
            
            # 2 choices: include curr num, or skip
            # choice 1:
            dfs(index, sum + nums[index], path + [nums[index]])
            # choice 2:
            dfs(index + 1, sum, path)
        
        dfs(0, 0, [])
        return result
