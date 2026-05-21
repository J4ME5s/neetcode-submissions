class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        leftLoc = 0
        rightLoc = len(height) - 1

        maxLeft = height[leftLoc]
        maxRight = height[rightLoc]

        totalArea = 0

        while leftLoc < rightLoc:
            if maxLeft <= maxRight:
                # move left
                leftLoc += 1
                if height[leftLoc] > maxLeft:
                    maxLeft = height[leftLoc]
                totalArea += (maxLeft - height[leftLoc])
            else:
                # move right
                rightLoc -= 1
                if height[rightLoc] > maxRight:
                    maxRight = height[rightLoc]
                totalArea += (maxRight - height[rightLoc])
        return totalArea

