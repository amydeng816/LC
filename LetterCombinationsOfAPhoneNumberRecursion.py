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
        results = []
        self.letterCombinationsRec(digits, d, "", results)
        return results

    def letterCombinationsRec(self, digits, d, s, results):
        if len(s) == len(digits):
            results.append(s)
            return
        for i in d[digits[len(s)]]:
            s = s + i
            self.letterCombinationsRec(digits, d, s, results)
            s = s[:len(s) - 1]