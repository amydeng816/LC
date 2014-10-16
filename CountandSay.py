class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        prev = '1'
        temp = ''
        for i in range(1, n):
            say = prev[0]
            count = 1
            temp = ''
            for j in range(1, len(prev)):
                if prev[j] != say:
                    temp = temp + str(count)
                    temp = temp + say
                    say = prev[j]
                    count = 1
                else:
                    count += 1
            temp = temp + str(count) + str(say)
            prev = temp
        return temp