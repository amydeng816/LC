class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if s == None or s == '':
            return 0
        positions = {}
        longest = 0
        repeat = -1
        for i in range(len(s)):
            if s[i] in positions and positions[s[i]] > repeat:
                repeat = positions[s[i]]
            if i - repeat > longest:
                longest = i - repeat
            positions[s[i]] = i
        return longest