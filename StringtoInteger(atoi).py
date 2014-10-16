class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if str == '':
            return 0
        sign = 1
        pos = 0
        if str[pos] == '-':
            sign = -1
            pos += 1
        elif str[pos] == '+':
            pos += 1
        num = 0
        while pos < len(str):
            if not str[pos].isdigit():
                break
            num = num * 10 + int(str[pos])
            pos += 1
        if sign > 0 and num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif sign < 0 and num > 2 ** 31:
            return -2 ** 31
        return sign * num 