
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        group = []
        for word in strs:
            x = ''.join(sorted(word))
            if x in d:
                group.append(word)
                if d[x] != -1:
                    group.append(strs[d[x]])
                    d[x] = -1
            else:
                d[x] = strs.index(word)
        return group

def main():
    s = Solution()
    print s.anagrams(["nozzle","punjabi","waterlogged","xruc","imprison","crux","numismatists","sultans"])
   
if __name__ == "__main__":
    main()