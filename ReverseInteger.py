class Solution:
    # @return an integer
    def reverse(self, x):
        minus = False
        if x < 0:
            minus = True
            x = -x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10
        if minus:
            return -y
        return y