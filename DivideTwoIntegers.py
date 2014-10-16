class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        dividend1 = self.abs(dividend)
        divisor1 = self.abs(divisor)
        ans = 0
        while dividend1 >= divisor1:
            shift = 0
            while dividend1 >= (divisor1 << shift):
                shift += 1
            shift -= 1
            dividend1 = dividend1 - (divisor1 << shift)
            ans = ans + (1 << shift)
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -ans
        return ans
        
    def abs(self, x):
        if x < 0:
            return -x
        return x