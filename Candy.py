class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        distribute = [1]
        sz = len(ratings)
        for i in range(1, sz):
            if ratings[i] > ratings[i - 1]:
                distribute.append(distribute[i - 1] + 1)
            else:
                distribute.append(1)
        i = sz - 2
        while i >= 0:
            if ratings[i + 1] < ratings[i]:
                distribute[i] = max(distribute[i], distribute[i + 1] + 1)
            i -= 1
        s = 0
        for i in distribute:
            s = s + i
        return s