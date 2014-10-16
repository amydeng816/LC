class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {}
        d["2"] = "abc"
        d["3"] = "def"
        d["4"] = "ghi"
        d["5"] = "jkl"
        d["6"] = "mno"
        d["7"] = "pqrs"
        d["8"] = "tuv"
        d["9"] = "wxyz"
        d["1"] = ""
        d["0"] = ""
        results = [""]
        for i in digits:
            s = d[i]
            result = []
            for string in results:
                for j in s:
                    result.append(string + j)
            results = result
        return results