class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxVolume = 0
        while start < end:
            dist = end - start
            minHeight = min(heights[start], heights[end])
            volume = dist * minHeight
            if volume > maxVolume:
                maxVolume = volume
            
            # move ptr that points to smaller val
            if minHeight == heights[start]:
                start += 1
            else:
                end -= 1
        return maxVolume