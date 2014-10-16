class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        group = []
        for word in strs:
            x = ''.join(sorted(word))
            if x in d: 
                d[x].append(word)
            else:
                d[x] = [word]
        for word in d:
            if len(d[word]) > 1:
                group = group + d[word]
        return group