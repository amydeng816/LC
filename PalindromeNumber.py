class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        ten = 10
        while x / ten >= 10:
            ten = ten * 10
        while ten > 1:
            if x % 10 != x / ten:
                return False
            x = (x - (x % 10) * ten) / 10
            ten = ten / 100
        return True