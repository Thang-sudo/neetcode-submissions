class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers, one start from 0 and the other starts from end of height list
        # area = min(height[i], height[j]) * (j - i)
        # if heigth[i] < height[j] => i += 1 and vice versa
        # Why do we move smaller height, because we wan to find the a better area. If we move the taller height, then the next area will be smaller. Area depends on the height of shortest column
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > max_area:
                max_area = area
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
            