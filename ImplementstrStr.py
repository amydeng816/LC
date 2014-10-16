class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if needle == "":
            return haystack
        ptr = 0
        lenhaystack = len(haystack)
        lenneedle = len(needle)
        while lenneedle <= lenhaystack - ptr:
            for i in range(lenneedle):
                if needle[i] != haystack[ptr + i]:
                    break
                if i == lenneedle - 1:
                    return haystack[ptr :]
            ptr += 1
        return None