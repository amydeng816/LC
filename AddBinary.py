class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        s = ''
        i = 0
        count = 0
        while i < len(a) or i < len(b):
            if i < len(a) and a[len(a) - i - 1] == '1':
                count += 1
            if i < len(b) and b[len(b) - i - 1] == '1':
                count += 1
            s = str(count % 2) + s
            count /= 2
            i += 1
        if count != 0:
            s = '1' + s
        return s
