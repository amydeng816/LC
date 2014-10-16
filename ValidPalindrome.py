class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.strip()
        if s == '':
            return True
        low = 0
        high = len(s) - 1
        while low <= high:
            if s[low].isalpha() or s[low].isdigit():
                low_char = s[low]
                if low_char.isalpha():
                    low_char = low_char.lower()
                while ((not s[high].isalpha()) and (not s[high].isdigit())) and high > low:
                    high -= 1
                high_char = s[high]
                if high_char.isalpha():
                    high_char = high_char.lower()
                if high_char != low_char:
                    return False
                high -= 1
            low += 1
        return True