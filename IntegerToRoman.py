class Solution:
    # @return a string
    def intToRoman(self, num):
        bit = num % 10
        ten = (num / 10) % 10
        hundred = (num / 100) % 10
        thousand = (num / 1000) % 10
        
        bit_str = self.intToRomanHelp(bit, 'I', 'V', 'X')
        ten_str = self.intToRomanHelp(ten, 'X', 'L', 'C')
        hundred_str = self.intToRomanHelp(hundred, 'C', 'D', 'M')
        result = hundred_str + ten_str + bit_str
        for i in range(thousand):
            result = 'M' + result
        return result
        
    def intToRomanHelp(self, digit, one, five, ten):
        result = ''
        if digit < 4:
            for i in range(digit):
                result = result + one
        elif digit == 4:
            result = one + five
        elif digit == 9:
            result = one + ten
        else:
            result = five
            for i in range(digit - 5):
                result = result + one
        return result