class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        if k == len(arr):
            res = arr
            return res
        
        l, r = 0, len(arr) - 1
        while (r - l + 1) > k:
            a = arr[l]
            b = arr[r]
            if (abs(a - x) < abs(b - x)):
                r -= 1
            elif (abs(a - x) > abs(b - x)):
                l += 1
            elif (abs(a - x) == abs(b - x)) and a < b:
                r -= 1
            else:
                l += 1
        res = arr[l:r+1]
        return res
        