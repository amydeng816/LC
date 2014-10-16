class Solution:
    def isValidWithoutE(self, s, decimalAllowed = True): 
        sz = len(s)
        if sz == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
            sz -= 1
            if sz == 0:
                return False
        digits = '0123456789'
        if '.' in s:
            if (not decimalAllowed) or sz == 1:
                return False
            i = s.index('.')
            s = s[:i] + s[i + 1:]
        for item in s:
            if item not in digits:
                return False
        return True

    def isNumber(self, s):
    ''' I. Before the main step, we need to strip s so that it does not include white spaces in the head and tail
    II. There are three main steps:
    1. number has e
    in this case, number in the left of e allows decimal, in the right is not allowed
    2. number has E
    the same case with e
    3. number does not have e or E
    in this case, decimal is allowed
    III. Then we need to use a function to tell if a number is valid without consider e or E(in both decimal case and not decimal case):
    1. check if s is empty
    2. if s has + or - in the head, delete it. check if s is empty after deletion
    3. check if s has . 
       if it has . and decimal is not allowed, return False. if it only has . return false
       check whether the rest part without . is digit'''
        s = s.strip()
        if 'e' in s:
            i = s.index('e')
            return self.isValidWithoutE(s[:i]) and self.isValidWithoutE(s[i + 1:], False)
        elif 'E' in s:
            i = s.index('E')
            return self.isValidWithoutE(s[:i]) and self.isValidWithoutE(s[i + 1:], False)
        else:
            return self.isValidWithoutE(s)