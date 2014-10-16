class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        if s == "":
            return False
        point = False
        minus = False
        if s[0] == '-' or s[0] == '+':
            minus = True
            s = s[1:]
        if s[0] == '.':
            point = True
            s = s[1:]
        if s == '':
            return False
        #print s
        e = 0
        if s[0] <= '9' and s[0] >= '0':
            e += 1
        for i in s:
            #print i
            if i == '-' or i == '+':
                if s.index(i) == len(s) - 1:
                    return False
                if not minus:
                    #print '==='
                    if s[s.index(i) - 1] != 'e':
                        return False
                    minus = True
                else:
                    #print '------'
                    return False
            elif i == '.':
                if e == 2:
                    return False
                if not point:
                    if s[s.index(i) - 1] > '9' or s[s.index(i) - 1] < '0':
                        return False
                    point = True
                else:
                    return False
            elif i == 'e':
                minus = False
                if s.index(i) == len(s) - 1:
                    return False
                elif e == 1:
                    e += 1
                else:
                    return False
            elif i > '9' or i < '0':
                return False
        return True