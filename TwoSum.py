class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if not num:
            return []
        d = {}
        i = 0
        while i < len(num):
            if num[i] in d:
                return [d[num[i]] + 1, i + 1]
            d[target - num[i]] = i
            i += 1
        return []