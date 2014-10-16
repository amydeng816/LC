class Solution:
    # @return an integer
    def romanToInt(self, s):
        if s == None or s == '':
            return 0
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        
        sz = len(s)
        result = d[s[sz - 1:]]
        ptr = sz - 2
        while ptr >= 0:
            if d[s[ptr + 1]] <= d[s[ptr]]:
                result += d[s[ptr]]
            else:
                result -= d[s[ptr]]
            ptr -= 1
        return result