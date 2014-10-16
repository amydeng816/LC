class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        arr = s.split(' ')
        arr = arr[::-1]
        i = 0
        s = ''
        while i in range(len(arr)):
            if arr[i] != '':
                s = s + ' ' + arr[i]  
            i += 1
        return s[1:]