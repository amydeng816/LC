class Solution:
    # @return an integer
    def maxArea(self, height):
        sz = len(height)
        begin = 0
        end = sz - 1
        m = 0
        while begin < end:
            temp = min(height[begin], height[end]) * (end - begin)
            if temp > m:
                m = temp
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1
        return m