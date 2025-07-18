class Solution:
    def maxArea(self, height: List[int]) -> int:
        # iterate from outside to inside
        left = 0
        right = len(height) - 1
        largestArea = 0
        while left < right:
            minheight = min(height[left], height[right])
            currArea = minheight * (right - left)
            largestArea = max(currArea, largestArea)
            # find which side is larger
            # increment the smalelr sider
            if height[left] > height[right]:
                right += -1
            else:
                left += 1
        return largestArea



