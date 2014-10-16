class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = ''
        pos = 0
        for i in strs[0]:
            for s in strs:
                if len(s) <= pos or s[pos] != i:
                    return prefix
            prefix += i
            pos += 1
        return prefix